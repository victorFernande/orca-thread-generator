import sys, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from thread_studio.schema import normalize_params
from thread_studio.thread_math import *


class ThreadMathTests(unittest.TestCase):
    def test_multistart_lead_and_handedness(self):
        for starts in (1, 2, 3):
            for hand, sign in [("right", 1), ("left", -1)]:
                p = normalize_params(dict(starts=starts, hand=hand, thread_length=60))
                self.assertEqual(p["lead"], p["pitch"] * starts)
                a = thread_radius(0.4, 30, p)
                b = thread_radius(0.7, 30 + sign * 0.3 * p["lead"] / (2 * np.pi), p)
                self.assertAlmostEqual(float(a), float(b), places=8)

    def test_higbee_blunts_both_ends(self):
        p = normalize_params()
        root = p["nominal_dia"] / 2 - thread_depth(p)
        for z in (0, p["thread_length"]):
            self.assertAlmostEqual(float(thread_radius(0, z, p)), root)
        self.assertAlmostEqual(float(higbee_envelope(0, 12, 2)), 0)
        self.assertAlmostEqual(float(higbee_envelope(6, 12, 2)), 1)

    def test_profile_flank_angles(self):
        for standard, slope in [("iso_metric", np.sqrt(3)), ("fdm_trapezoid_45", 1)]:
            p = normalize_params(dict(standard=standard, nominal_dia=40, pitch=3))
            a = float(thread_profile(0.2, standard)) * thread_depth(p)
            b = float(thread_profile(0.25, standard)) * thread_depth(p)
            self.assertAlmostEqual((a - b) / (0.05 * p["pitch"]), slope, places=5)

    def test_female_envelope_clearance(self):
        for standard in ("iso_metric", "fdm_trapezoid_45", "pco1881", "mason_70"):
            for starts in (1, 2, 3):
                p = normalize_params(
                    dict(
                        standard=standard,
                        starts=starts,
                        diametral_clearance=0.05,
                        axial_clearance=0,
                    )
                )
                report = analyze_engagement(p)
                self.assertFalse(report["interference"])
                self.assertGreaterEqual(report["minimum_radial_gap_mm"], 0.024999)

    def test_invalid_normalization_and_mason_confirmation(self):
        p = normalize_params(
            dict(
                nominal_dia=float("nan"),
                pitch=float("inf"),
                starts=7,
                height=-4,
                wall_thickness=0,
            )
        )
        self.assertEqual(p["nominal_dia"], 40)
        self.assertEqual(p["pitch"], 3)
        self.assertEqual(p["starts"], 3)
        self.assertGreaterEqual(p["wall_thickness"], 1.2)
        with self.assertRaises(ValueError):
            normalize_params(
                dict(
                    module="standard_bottle_cap",
                    standard="mason_86",
                    measurements_confirmed=True,
                )
            )
        measured = normalize_params(
            dict(
                module="standard_bottle_cap",
                standard="mason_86",
                measurements_confirmed=True,
                measured_major_dia=85,
                measured_root_dia=82,
                measured_pitch=6,
                measured_length=10,
            )
        )
        self.assertEqual(measured["nominal_dia"], 85)
        self.assertEqual(thread_depth(measured), 1.5)

    def test_mason_measurement_limits_prevent_extreme_meshes(self):
        for measured_pitch, measured_length in [(0.0001, 40), (1, 0.01)]:
            with self.assertRaises(ValueError):
                normalize_params(
                    dict(
                        module="standard_bottle_cap",
                        standard="mason_86",
                        measurements_confirmed=True,
                        measured_major_dia=86,
                        measured_root_dia=82,
                        measured_pitch=measured_pitch,
                        measured_length=measured_length,
                    )
                )

    def test_pco_is_separate_experimental_envelope(self):
        p = normalize_params(dict(module="standard_bottle_cap", standard="pco1881"))
        self.assertEqual((p["nominal_dia"], p["pitch"], p["starts"]), (27.4, 2.7, 1))
        self.assertAlmostEqual(thread_depth(p), 1.6)
        self.assertNotEqual(
            float(thread_profile(-0.2, "pco1881")),
            float(thread_profile(0.2, "pco1881")),
        )
        self.assertTrue(analyze_engagement(p)["experimental"])


if __name__ == "__main__":
    unittest.main()
