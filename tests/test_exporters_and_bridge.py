import sys, unittest, tempfile, struct, zipfile, json, importlib.util, subprocess, shutil, threading
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from thread_studio.mesh_generator import generate_parts
from thread_studio.exporters import write_binary_stl, write_orca_3mf
from thread_studio.presets_catalog import *
from thread_studio.plugin_main import (
    ThreadStudioController,
    OrcaThreadStudioPlugin,
    ThreadStudioPageCapability,
    ThreadStudioDockCapability,
)
from thread_studio.studio_ui import get_studio_html
import thread_studio.plugin_main as bridge

ROOT = Path(__file__).resolve().parents[1]


class ExportBridgeTests(unittest.TestCase):
    def test_binary_stl_and_multibody_3mf(self):
        items = generate_parts(dict(resolution=48))
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            stl = write_binary_stl(base / "a.stl", items[0][1])
            data = stl.read_bytes()
            count = struct.unpack("<I", data[80:84])[0]
            self.assertEqual(len(data), 84 + 50 * count)
            path = write_orca_3mf(
                base / "a.3mf",
                items,
                normalize_params(),
                dict(bed_x=220, bed_y=220, max_z=250),
            )
            with zipfile.ZipFile(path) as z:
                names = z.namelist()
                self.assertIn("3D/3dmodel.model", names)
                self.assertIn("Metadata/project_settings.config", names)
                settings = json.loads(z.read("Metadata/project_settings.config"))
                self.assertEqual(settings["spiral_mode"], "0")
                self.assertEqual(settings["wall_loops"], "5")

    def test_reject_nonfinite_and_out_of_bed(self):
        mesh = generate_parts(dict(resolution=48))[0][1]
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                write_orca_3mf(
                    Path(d) / "small.3mf", [("a", mesh)], {}, dict(bed_x=20, bed_y=20)
                )
            mesh.vertices[0, 0] = float("nan")
            with self.assertRaises(ValueError):
                write_binary_stl(Path(d) / "invalid.stl", mesh)

    def test_atomic_user_presets(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(load_user_presets(d), [])
            saved = save_user_preset(d, "Test", dict(starts=3))
            self.assertEqual(saved[0]["params"]["starts"], 3)
            self.assertEqual(delete_user_preset(d, saved[0]["id"]), [])
            self.assertFalse((Path(d) / "user_presets.tmp").exists())

    def test_registration_page_dock_icon(self):
        OrcaThreadStudioPlugin().register_capabilities()
        self.assertEqual(bridge.orca._requested_permissions, dict(threading=True))
        self.assertIn(ThreadStudioPageCapability, bridge.orca._registered_capabilities)
        self.assertIn(ThreadStudioDockCapability, bridge.orca._registered_capabilities)
        with (
            tempfile.TemporaryDirectory() as d,
            patch.object(bridge, "_resolve_storage_dir", return_value=Path(d)),
        ):
            cap = ThreadStudioPageCapability()
            self.assertTrue(Path(cap.get_icon()).is_file())
            self.assertIn("Orca Thread Studio", cap.get_ui())

    def test_shared_undo_redo_and_invalid_commands(self):
        c = ThreadStudioController()
        a = []
        b = []
        c.handle_message(dict(type="ready"), a.append)
        c._last_geometry_worker.join()
        c.handle_message(dict(type="ready"), b.append)
        c._last_geometry_worker.join()
        p = c.current_params
        p["pitch"] = 4
        c.handle_message(dict(type="update", params=p), a.append)
        c._last_geometry_worker.join()
        self.assertEqual(b[-2]["params"]["pitch"], 4)
        c.handle_message(dict(type="undo"), a.append)
        c._last_geometry_worker.join()
        self.assertEqual(c.current_params["pitch"], 3)
        c.handle_message(dict(type="redo"), a.append)
        c._last_geometry_worker.join()
        self.assertEqual(c.current_params["pitch"], 4)
        c.handle_message("invalid-json", a.append)
        self.assertFalse(a[-1]["ok"])

    def test_no_success_before_transport_returns(self):
        c = ThreadStudioController()
        out = []
        entered = threading.Event()
        release = threading.Event()

        def transport(paths):
            entered.set()
            release.wait(5)
            return False, "test refusal", None

        with (
            patch.object(c, "_write_exports", return_value=["example.3mf"]),
            patch.object(bridge, "_dispatch_files_to_plater", side_effect=transport),
        ):
            c.handle_message(dict(type="send_to_plater"), out.append)
            self.assertTrue(entered.wait(5))
            self.assertIsNone(out[-1]["ok"])
            release.set()
            c._last_plater_worker.join(5)
            self.assertFalse(out[-1]["ok"])
        self.assertEqual(out[-1]["message"], "Transport failed.")
        self.assertIn("test refusal", out[-1]["detail"])

    def test_html_javascript_syntax_and_offline(self):
        html = get_studio_html()
        self.assertNotIn('src="http', html)
        self.assertNotIn('href="http', html)
        if shutil.which("node"):
            script = html.split("<script>", 1)[1].split("</script>", 1)[0]
            with tempfile.TemporaryDirectory() as d:
                path = Path(d) / "ui.js"
                path.write_text(script, encoding="utf-8")
                result = subprocess.run(
                    ["node", "--check", str(path)], capture_output=True, text=True, encoding="utf-8"
                )
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_loupe_profile_matches_numpy_equations(self):
        if not shutil.which("node"):
            self.skipTest("Node.js unavailable")
        from thread_studio.thread_math import thread_radius
        import numpy as np

        for standard in ("iso_metric", "fdm_trapezoid_45", "pco1881"):
            params = normalize_params(dict(standard=standard, axial_clearance=0.2))
            html = get_studio_html(initial_context=dict(params=params))
            source = html.split("<script>", 1)[1].split("</script>", 1)[0]
            values = np.linspace(0.01, params["thread_length"] - 0.01, 81)
            program = (
                source
                + ";process.stdout.write(JSON.stringify("
                + json.dumps(values.tolist())
                + ".map(q=>[__threadStudio.radialProfile(q,false),__threadStudio.radialProfile(q,true)])));"
            )
            result = subprocess.run(
                ["node"], input=program, capture_output=True, text=True, encoding="utf-8"
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            expected = np.c_[
                thread_radius(0, values, params), thread_radius(0, values, params, True)
            ]
            np.testing.assert_allclose(json.loads(result.stdout), expected, atol=1e-10)

    def test_latest_preview_revision_and_reset(self):
        c = ThreadStudioController()
        out = []
        c._listeners.append(out.append)
        entered = threading.Event()
        release = threading.Event()
        calls = []

        def geometry(params):
            calls.append(params["pitch"])
            if len(calls) == 1:
                entered.set()
                release.wait(5)
            return dict(type="geometry", params=params)

        with patch.object(c, "_geometry_message", side_effect=geometry):
            c.handle_message(dict(type="update", params=dict(pitch=4)), out.append)
            first = c._last_geometry_worker
            self.assertTrue(entered.wait(5))
            c.handle_message(dict(type="update", params=dict(pitch=5)), out.append)
            second = c._last_geometry_worker
            release.set()
            first.join(5)
            second.join(5)
            completed = [m for m in out if m["type"] == "geometry"]
            self.assertEqual(len(completed), 1)
            self.assertEqual(completed[0]["params"]["pitch"], 5)
        c.handle_message(dict(type="reset"), out.append)
        c._last_geometry_worker.join(10)
        self.assertEqual(c.current_params["pitch"], 3)

    def test_bundle_and_wheel_isolated(self):
        spec = importlib.util.spec_from_file_location(
            "thread_builder", ROOT / "scripts/build_and_install.py"
        )
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        bundle = builder.build_bundle()
        wheel = builder.build_wheel()
        builder.verify_bundle_smoke(bundle)
        builder.verify_wheel_smoke(wheel)


if __name__ == "__main__":
    unittest.main()
