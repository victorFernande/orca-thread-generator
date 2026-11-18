import sys, unittest, itertools
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from thread_studio.mesh_generator import *
from thread_studio.thread_math import thread_radius, thread_depth
from thread_studio.presets_catalog import BUILTIN_PRESETS


def section_radii(mesh, z, directions):
    faces = mesh.vertices[mesh.triangles].astype(float)
    segments = []
    for face in faces:
        intersections = []
        for a, b in zip(face, np.roll(face, -1, axis=0)):
            if (a[2] < z <= b[2]) or (b[2] < z <= a[2]):
                intersections.append((a + (b - a) * (z - a[2]) / (b[2] - a[2]))[:2])
        if len(intersections) == 2:
            segments.append(intersections)
    edges = np.asarray(segments)
    a = edges[:, 0]
    e = edges[:, 1] - a
    d = directions[:, None, :]
    cross = lambda x, y: x[..., 0] * y[..., 1] - x[..., 1] * y[..., 0]
    denominator = cross(d, e[None, :, :])
    valid = np.abs(denominator) > 1e-10
    den = np.where(valid, denominator, 1)
    radial = cross(a, e)[None, :] / den
    u = cross(a[None, :, :], d) / den
    valid &= (u >= -1e-7) & (u <= 1 + 1e-7) & (radial > 0)
    return np.min(np.where(valid, radial, np.inf), axis=1), np.max(
        np.where(valid, radial, -np.inf), axis=1
    )


class GeometryTests(unittest.TestCase):
    def assert_mesh(self, m, euler):
        v = m.vertices
        t = m.triangles
        self.assertTrue(np.isfinite(v).all())
        self.assertGreater(m.volume_cm3, 0)
        cross = np.cross(v[t[:, 1]] - v[t[:, 0]], v[t[:, 2]] - v[t[:, 0]])
        self.assertTrue((np.linalg.norm(cross, axis=1) > 1e-9).all())
        edges = np.concatenate([t[:, [0, 1]], t[:, [1, 2]], t[:, [2, 0]]])
        unique, counts = np.unique(np.sort(edges, axis=1), axis=0, return_counts=True)
        self.assertTrue((counts == 2).all())
        self.assertEqual(len(v) - len(unique) + len(t), euler)
        forward = np.where(edges[:, 0] < edges[:, 1], 1, -1)
        _, ids = np.unique(np.sort(edges, axis=1), axis=0, return_inverse=True)
        self.assertTrue((np.bincount(ids, weights=forward) == 0).all())
        self.assertEqual(len(np.unique(t)), len(v))
        np.testing.assert_allclose(np.linalg.norm(m.face_normals, axis=1), 1, atol=2e-6)

    def test_all_presets_closed_and_mason86_blocked(self):
        self.assertEqual(len(BUILTIN_PRESETS), 12)
        for preset in BUILTIN_PRESETS:
            p = dict(preset["params"], resolution=48)
            if preset["id"] == "mason86":
                with self.assertRaisesRegex(ValueError, "Mason 86"):
                    generate_parts(p)
                continue
            for name, m in generate_parts(p):
                with self.subTest(preset=preset["id"], part=name):
                    self.assert_mesh(m, 0 if name in ("Adapter", "Nut", "Neck") else 2)

    def test_all_adapter_end_combinations(self):
        for a, b in itertools.product(("smooth", "barb", "male", "female"), repeat=2):
            p = dict(module="hose_vacuum_adapter", end_a=a, end_b=b, resolution=48)
            self.assert_mesh(generate_parts(p)[0][1], 0)

    def test_bolt_heads_hand_starts_and_bores(self):
        for head, hand, starts in itertools.product(
            ("hex", "wing", "knurled"), ("right", "left"), (1, 3)
        ):
            for name, m in generate_parts(
                dict(
                    module="bolt_nut_knob",
                    head=head,
                    hand=hand,
                    starts=starts,
                    bore_diameter=6,
                    resolution=48,
                )
            ):
                self.assert_mesh(m, 0)

    def test_kit_has_three_physical_notch_patterns(self):
        rings = generate_thread_calibration_kit(dict(resolution=96))
        self.assertEqual(len(rings), 3)
        for index, (name, m) in enumerate(rings, 1):
            self.assert_mesh(m, 0)
            self.assertIn(f"Ring_{index}", name)
            # On the outer top ring, count radial valleys separated by full-radius vertices.
            top = m.vertices[np.abs(m.vertices[:, 2] - m.bounds_mm["max"][2]) < 1e-6]
            r = np.linalg.norm(top[:96, :2], axis=1)
            valleys = r < r.max() - 0.1
            count = np.sum(valleys & ~np.roll(valleys, 1))
            self.assertEqual(count, index)

    def test_faceted_wall_is_not_inverted(self):
        p = normalize_params(
            dict(
                nominal_dia=100,
                pitch=0.5,
                diameter=12,
                wall_thickness=1.2,
                texture="faceted",
                resolution=48,
            )
        )
        parts = generate_parts(p)
        for name, m in parts:
            self.assert_mesh(m, 2)
        jar = parts[0][1]
        _, outer = section_radii(
            jar,
            6,
            np.c_[
                np.cos(np.arange(300) * 2 * np.pi / 300),
                np.sin(np.arange(300) * 2 * np.pi / 300),
            ],
        )
        self.assertGreaterEqual(
            float(outer.min()), p["nominal_dia"] / 2 - thread_depth(p) - 1e-4
        )

    def test_impossible_wall_rejected(self):
        with self.assertRaisesRegex(ValueError, "bore"):
            generate_parts(
                dict(
                    module="hose_vacuum_adapter",
                    inlet_diameter=10,
                    outlet_diameter=10,
                    wall_thickness=8,
                    pitch=10,
                    end_a="male",
                    end_b="male",
                    resolution=48,
                )
            )
        with self.assertRaisesRegex(ValueError, "bore"):
            generate_parts(dict(nominal_dia=6, wall_thickness=8, resolution=48))

    def test_exported_surfaces_fit_after_cap_inversion(self):
        angles = np.linspace(0.001, 2 * np.pi + 0.001, 301)
        directions = np.c_[np.cos(angles), np.sin(angles)]
        for starts in (1, 3):
            p = normalize_params(
                dict(
                    thread_length=36,
                    starts=starts,
                    resolution=48,
                    diametral_clearance=0.05,
                    axial_clearance=0,
                    gasket=False,
                    texture="smooth",
                )
            )
            (_, jar), (_, lid) = generate_parts(p)
            lid.vertices = lid.vertices.copy()
            lid.vertices[:, 1] *= -1
            lid.vertices[:, 2] = p["height"] + p["floor_thickness"] - lid.vertices[:, 2]
            for q in (17.03, 18.125, 19.125):
                z = p["height"] - p["thread_length"] + q
                male = section_radii(jar, z, directions)[1]
                female = section_radii(lid, z, directions)[0]
                self.assertGreaterEqual(float(np.min(female - male)), 0.0248)


if __name__ == "__main__":
    unittest.main()
