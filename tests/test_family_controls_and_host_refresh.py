"""Behavioral regressions for the canonical-template Thread Studio controls."""

import copy
import json
from html.parser import HTMLParser
import shutil
import subprocess
import sys
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from thread_studio.schema import normalize_params
from thread_studio.mesh_generator import generate_parts
from thread_studio.presets_catalog import (
    BUILTIN_PRESETS,
    generate_random_printable_params,
)
from thread_studio.plugin_main import ThreadStudioController
from thread_studio.studio_ui import get_studio_html


class ElementTreeParser(HTMLParser):
    """Small DOM tree for structural regressions without browser dependencies."""

    def __init__(self):
        super().__init__()
        self.root = dict(tag="root", attrs={}, children=[])
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = dict(tag=tag, attrs=dict(attrs), children=[])
        self.stack[-1]["children"].append(node)
        if tag not in {"input", "meta", "link", "br", "hr", "img", "source"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                return

    def nodes(self, node=None):
        node = self.root if node is None else node
        yield node
        for child in node["children"]:
            yield from self.nodes(child)


class CanonicalCutBarTests(unittest.TestCase):
    def test_cut_bar_has_only_canonical_mode_buttons_and_no_wrapping_extra_control(
        self,
    ):
        parser = ElementTreeParser()
        parser.feed(get_studio_html())
        bar = next(
            node
            for node in parser.nodes()
            if "vp-cut-bar" in node["attrs"].get("class", "").split()
        )
        direct_buttons = [node for node in bar["children"] if node["tag"] == "button"]
        self.assertEqual(
            [node["attrs"]["id"] for node in direct_buttons],
            ["btn-cut-half", "btn-cut-off"],
        )
        mode_group = next(
            node
            for node in bar["children"]
            if "vp-cut-modes" in node["attrs"].get("class", "").split()
        )
        modes = [node for node in mode_group["children"] if node["tag"] == "button"]
        self.assertEqual(
            [node["attrs"]["id"] for node in modes], ["cut", "btn-cut-mode-z"]
        )
        self.assertTrue(
            all(
                "vp-cut-mode-btn" in node["attrs"].get("class", "").split()
                for node in modes
            )
        )
        # An extra .vp-chip previously wrapped and raised the bar over the camera pills.
        self.assertFalse(
            any(
                "vp-chip" in node["attrs"].get("class", "").split()
                for node in parser.nodes(bar)
            )
        )


class FamilyControlsTests(unittest.TestCase):
    def test_surprise_preserves_each_family_and_generates_valid_parts(self):
        for family in (
            "container_and_lid",
            "standard_bottle_cap",
            "hose_vacuum_adapter",
            "bolt_nut_knob",
        ):
            for seed in range(8):
                with self.subTest(family=family, seed=seed):
                    original = normalize_params(dict(module=family, resolution=48))
                    result = generate_random_printable_params(seed, original)
                    self.assertEqual(result["module"], family)
                    self.assertEqual(result["standard"], original["standard"])
                    self.assertFalse(result["measurements_confirmed"])
                    parts = generate_parts(result)
                    self.assertTrue(parts)
                    self.assertTrue(all(mesh.volume_cm3 > 0 for _, mesh in parts))

    def test_surprise_is_deterministic_and_does_not_mutate_presets(self):
        before = copy.deepcopy(BUILTIN_PRESETS)
        for preset in BUILTIN_PRESETS:
            first = generate_random_printable_params(42, preset["params"])
            second = generate_random_printable_params(42, preset["params"])
            self.assertEqual(first, second)
        self.assertEqual(BUILTIN_PRESETS, before)

    def test_bottle_standard_dimensions_stay_fixed(self):
        for standard, dimensions in [
            ("pco1881", (27.4, 2.7, 7.0)),
            ("mason_70", (70.0, 6.35, 7.9375)),
        ]:
            for seed in range(8):
                result = generate_random_printable_params(
                    seed, dict(module="standard_bottle_cap", standard=standard)
                )
                self.assertEqual(
                    (result["nominal_dia"], result["pitch"], result["thread_length"]),
                    dimensions,
                )
                self.assertFalse(result["measurements_confirmed"])
                self.assertTrue(generate_parts(dict(result, resolution=48)))

    def test_mason86_surprise_cannot_unlock_measurements(self):
        original = normalize_params(
            dict(
                module="standard_bottle_cap",
                standard="mason_86",
                measurements_confirmed=True,
                measured_major_dia=86,
                measured_root_dia=82,
                measured_pitch=6,
                measured_length=10,
            )
        )
        for seed in range(8):
            result = generate_random_printable_params(seed, original)
            self.assertEqual(result["standard"], "mason_86")
            self.assertEqual(result["module"], "standard_bottle_cap")
            self.assertFalse(result["measurements_confirmed"])
            with self.assertRaisesRegex(ValueError, "confirm"):
                generate_parts(result)

    def test_geometry_replies_correlate_clients_without_changing_parameters(self):
        controller = ThreadStudioController()
        messages = []
        controller._listeners.append(messages.append)
        with patch.object(
            controller,
            "_geometry_message",
            return_value=dict(type="geometry", params=controller.current_params),
        ):
            controller.handle_message(
                dict(
                    type="update",
                    params=controller.current_params,
                    client_id="page",
                    request_id=7,
                ),
                messages.append,
            )
            controller._last_geometry_worker.join(5)
            controller.handle_message(
                dict(
                    type="update",
                    params=controller.current_params,
                    client_id="dock",
                    request_id=3,
                ),
                messages.append,
            )
            controller._last_geometry_worker.join(5)
        payload = [message for message in messages if message["type"] == "geometry"][-1]
        self.assertEqual(payload["client_id"], "dock")
        self.assertEqual(payload["request_id"], 3)
        self.assertEqual(payload["client_acknowledgements"], dict(page=7, dock=3))
        self.assertNotIn("client_id", controller.current_params)
        self.assertNotIn("request_id", controller.current_params)

    def test_preview_acknowledgements_belong_to_the_parameter_snapshot(self):
        controller = ThreadStudioController()
        messages = []
        entered = threading.Event()
        release = threading.Event()
        controller._listeners.append(messages.append)

        def compute(params):
            entered.set()
            release.wait(5)
            return dict(type="geometry", params=params)

        with patch.object(controller, "_geometry_message", side_effect=compute):
            controller._queue_geometry(1, "page")
            self.assertTrue(entered.wait(5))
            # Interleave a newer committed input before its preview is queued.
            with controller._lock:
                controller._client_requests["page"] = 2
                controller.set_current_params(dict(nominal_dia=42))
            release.set()
            controller._last_geometry_worker.join(5)
        payload = [message for message in messages if message["type"] == "geometry"][-1]
        self.assertEqual(payload["params"]["nominal_dia"], 40)
        self.assertEqual(payload["client_acknowledgements"]["page"], 1)
        self.assertEqual(controller.current_params["nominal_dia"], 42)

    def test_sync_printer_refreshes_host_without_touching_design_or_geometry(self):
        controller = ThreadStudioController()
        controller.set_current_params(dict(nominal_dia=48, pitch=4, starts=3))
        before = controller.current_params
        history = copy.deepcopy(controller._undo)
        messages = []
        refreshed = dict(
            printer_name="Refreshed printer",
            bed_x=256,
            bed_y=256,
            max_z=256,
            nozzle_mm=0.6,
            lang="en",
            theme="light",
        )
        with (
            patch.object(controller, "read_host_context", return_value=refreshed),
            patch.object(controller, "_queue_geometry") as geometry,
        ):
            controller.handle_message(dict(type="sync_printer"), messages.append)
        self.assertEqual(messages, [dict(type="host_state", host=refreshed)])
        self.assertEqual(controller.current_params, before)
        self.assertEqual(controller._undo, history)
        geometry.assert_not_called()


@unittest.skipUnless(shutil.which("node"), "Node.js unavailable")
class CameraAndBootTests(unittest.TestCase):
    def run_javascript(self, suffix, params=None):
        html = get_studio_html(initial_context=dict(params=normalize_params(params)))
        script = html.split("<script>", 1)[1].split("</script>", 1)[0]
        result = subprocess.run(
            ["node"], input=script + suffix, text=True, encoding="utf-8", capture_output=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_assembly_bounds_include_the_inverted_and_translated_lid(self):
        suffix = ";const parts=[{bounds:{min:[-20,-20,0],max:[20,20,55],size:[40,40,55]}},{bounds:{min:[-23,-23,0],max:[23,23,14.4],size:[46,46,14.4]}}];process.stdout.write(JSON.stringify(__threadStudio.getSceneBounds(parts)));"
        bounds = self.run_javascript(suffix)
        self.assertAlmostEqual(bounds["min"][2], 0)
        self.assertAlmostEqual(bounds["max"][2], 65.4, places=5)
        self.assertEqual(bounds["min"][0], -23)
        self.assertEqual(bounds["max"][0], 23)

    def test_calibration_bounds_include_all_three_separated_rings(self):
        suffix = ";const part={bounds:{min:[-20,-20,0],max:[20,20,5],size:[40,40,5]}};process.stdout.write(JSON.stringify(__threadStudio.getSceneBounds([part,part,part])));"
        bounds = self.run_javascript(suffix, dict(export_target="calibration"))
        self.assertAlmostEqual(bounds["min"][0], -66)
        self.assertAlmostEqual(bounds["max"][0], 66)
        self.assertAlmostEqual(bounds["size"][0], 132)

    def test_all_camera_directions_use_complete_scene_bounds(self):
        # Camera fitting consumes the same transformed scene bounds as calipers/HUD.
        result = self.run_javascript(
            ";process.stdout.write(JSON.stringify({state:__threadStudio.getState(),bounds:__threadStudio.fitCamera()}));"
        )
        self.assertEqual(result["state"]["view"]["zoom"], 1)
        self.assertTrue(all(value > 0 for value in result["bounds"]["size"]))

    def test_older_geometry_cannot_overwrite_a_newer_unsent_edit(self):
        suffix = ";const stale=__threadStudio.geometryRevisionIsStale;process.stdout.write(JSON.stringify([stale({client_id:'page',request_id:2},'page',3,1),stale({client_id:'page',request_id:3},'page',3,1),stale({client_id:'dock',request_id:2},'page',3,1),stale({client_id:'dock',request_id:2,client_acknowledgements:{page:3}},'page',3,1)]));"
        self.assertEqual(self.run_javascript(suffix), [True, False, True, False])

    def test_toolbar_pending_edit_is_atomic_and_late_updates_cannot_undo_it(self):
        current = normalize_params(dict(nominal_dia=44))
        suffix = (
            ";process.stdout.write(JSON.stringify(__threadStudio.buildMutationPayload({type:'undo'},"
            + json.dumps(current)
            + ",2,1,'page')));"
        )
        message = self.run_javascript(suffix)
        self.assertEqual(message["type"], "undo")
        self.assertEqual(message["pending_params"]["nominal_dia"], 44)
        self.assertEqual(message["request_id"], 3)
        controller = ThreadStudioController()
        with patch.object(controller, "_queue_geometry"):
            controller.handle_message(
                dict(
                    type="update",
                    params=dict(nominal_dia=42),
                    request_id=1,
                    client_id="page",
                ),
                lambda _: None,
            )
            controller.handle_message(message, lambda _: None)
            self.assertEqual(controller.current_params["nominal_dia"], 42)
            # Simulate an earlier HTTP update arriving AFTER the toolbar command.
            controller.handle_message(
                dict(type="update", params=current, request_id=2, client_id="page"),
                lambda _: None,
            )
            self.assertEqual(controller.current_params["nominal_dia"], 42)
            controller.handle_message(
                dict(type="redo", request_id=4, client_id="page"), lambda _: None
            )
            self.assertEqual(controller.current_params["nominal_dia"], 44)

    def test_reset_and_surprise_preserve_the_pending_edit_in_undo_history(self):
        current = normalize_params(dict(nominal_dia=44))
        for action in ("reset", "randomize"):
            with self.subTest(action=action):
                payload = dict(type=action, params=current, seed=2)
                suffix = (
                    ";process.stdout.write(JSON.stringify(__threadStudio.buildMutationPayload("
                    + json.dumps(payload)
                    + ","
                    + json.dumps(current)
                    + ",2,1,'page')));"
                )
                message = self.run_javascript(suffix)
                controller = ThreadStudioController()
                with patch.object(controller, "_queue_geometry"):
                    controller.handle_message(
                        dict(
                            type="update",
                            params=dict(nominal_dia=42),
                            request_id=1,
                            client_id="page",
                        ),
                        lambda _: None,
                    )
                    controller.handle_message(message, lambda _: None)
                    self.assertNotEqual(controller.current_params["nominal_dia"], 44)
                    controller.handle_message(
                        dict(type="undo", request_id=4, client_id="page"),
                        lambda _: None,
                    )
                    self.assertEqual(controller.current_params["nominal_dia"], 44)

    def test_late_initial_state_preserves_edits_and_theme_but_refreshes_metadata(self):
        current = dict(
            params=normalize_params(dict(nominal_dia=44)),
            lang="en",
            theme="light",
            host=dict(printer_name="Old"),
            userPresets=[],
            builtins=[],
        )
        incoming = dict(
            type="init_state",
            request_id=0,
            client_id="page",
            params=normalize_params(),
            lang="pt",
            theme="dark",
            host=dict(printer_name="Refreshed"),
            user_presets=[dict(id="new")],
            builtin_presets=[dict(id="builtin")],
        )
        for acknowledged in (0, 1):
            suffix = (
                ";process.stdout.write(JSON.stringify(__threadStudio.resolveInitialState("
                + json.dumps(incoming)
                + ","
                + json.dumps(current)
                + ",'page',1,"
                + str(acknowledged)
                + ")));"
            )
            result = self.run_javascript(suffix)
            self.assertFalse(result["acceptDesign"])
            self.assertEqual(result["params"]["nominal_dia"], 44)
            self.assertEqual((result["lang"], result["theme"]), ("en", "light"))
            self.assertEqual(result["host"]["printer_name"], "Refreshed")
            self.assertEqual(result["userPresets"], [dict(id="new")])
            self.assertEqual(result["builtins"], [dict(id="builtin")])

    def test_initial_state_applies_before_any_local_edit(self):
        incoming = dict(
            type="init_state",
            request_id=0,
            client_id="page",
            params=normalize_params(dict(nominal_dia=48)),
            lang="en",
            theme="light",
        )
        current = dict(
            params=normalize_params(),
            lang="pt",
            theme="dark",
            host={},
            userPresets=[],
            builtins=[],
        )
        suffix = (
            ";process.stdout.write(JSON.stringify(__threadStudio.resolveInitialState("
            + json.dumps(incoming)
            + ","
            + json.dumps(current)
            + ",'page',0,0)));"
        )
        result = self.run_javascript(suffix)
        self.assertTrue(result["acceptDesign"])
        self.assertEqual(result["params"]["nominal_dia"], 48)
        self.assertEqual((result["lang"], result["theme"]), ("en", "light"))

    def test_server_rendered_light_theme_and_language_match_boot_state(self):
        html = get_studio_html("dock", dict(theme="light", lang="en"))
        self.assertIn('<html lang="en" data-theme="light">', html)
        self.assertIn('data-mode="dock"', html)
        script = html.split("<script>", 1)[1].split("</script>", 1)[0]
        result = subprocess.run(
            ["node"],
            input=script
            + ";process.stdout.write(JSON.stringify(__threadStudio.getState()));",
            text=True, encoding="utf-8",
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        state = json.loads(result.stdout)
        self.assertEqual((state["theme"], state["lang"]), ("light", "en"))
        self.assertEqual(
            (state["params"]["theme"], state["params"]["lang"]), ("light", "en")
        )


if __name__ == "__main__":
    unittest.main()
