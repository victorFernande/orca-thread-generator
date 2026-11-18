"""Regression cases for the 1.0.1 export and installation fixes."""

import importlib.util
import os
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from thread_studio.mesh_generator import generate_parts
from thread_studio.exporters import write_orca_3mf


def load_builder():
    spec = importlib.util.spec_from_file_location(
        "thread_patch_builder", ROOT / "scripts/build_and_install.py"
    )
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    return builder


class PatchExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mesh = generate_parts(dict(resolution=48))[0][1]

    def test_explicit_invalid_limits_never_use_defaults(self):
        keys = ("bed_x", "bed_y", "max_z", "bed_z", "printable_height")
        invalid = (None, 0, -1, float("nan"), float("inf"), "bad", True)
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "invalid.3mf"
            for key in keys:
                for value in invalid:
                    for nested in (False, True):
                        config = {"printer": {key: value}} if nested else {key: value}
                        with self.subTest(key=key, value=repr(value), nested=nested):
                            with self.assertRaisesRegex(ValueError, "printable limit"):
                                write_orca_3mf(
                                    destination, [("Part", self.mesh)], {}, config
                                )
                            self.assertFalse(destination.exists())

    def test_invalid_lower_priority_alias_is_still_rejected(self):
        cases = [
            dict(max_z=250, bed_z=0),
            dict(max_z=250, printable_height=None),
            dict(bed_x=220, printer=dict(bed_x="bad")),
            dict(max_z=250, printer=dict(bed_z=float("nan"))),
        ]
        with tempfile.TemporaryDirectory() as directory:
            for config in cases:
                with self.subTest(config=config), self.assertRaises(ValueError):
                    write_orca_3mf(
                        Path(directory) / "invalid.3mf",
                        [("Part", self.mesh)],
                        {},
                        config,
                    )

    def test_height_aliases_and_presence_precedence(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "height.3mf"
            for key in ("max_z", "bed_z", "printable_height"):
                for nested in (False, True):
                    config = {"printer": {key: 10}} if nested else {key: 10}
                    with (
                        self.subTest(key=key, nested=nested),
                        self.assertRaisesRegex(ValueError, "height"),
                    ):
                        write_orca_3mf(destination, [("Part", self.mesh)], {}, config)
            # Valid aliases are selected by documented presence order, never truthiness.
            write_orca_3mf(
                destination,
                [("Part", self.mesh)],
                {},
                dict(max_z=250, bed_z=10, printable_height=5),
            )
            self.assertTrue(destination.is_file())
            destination.unlink()
            write_orca_3mf(
                destination,
                [("Part", self.mesh)],
                {},
                dict(bed_z=250, printer=dict(max_z=10)),
            )
            self.assertTrue(destination.is_file())

    def test_only_absent_limits_receive_defaults(self):
        with tempfile.TemporaryDirectory() as directory:
            for index, config in enumerate(
                (None, {}, dict(bed_x=220), dict(printer={}))
            ):
                destination = Path(directory) / f"default_{index}.3mf"
                write_orca_3mf(destination, [("Part", self.mesh)], {}, config)
                self.assertTrue(destination.is_file())

    def test_xml_invalid_object_names_and_project_titles_are_rejected(self):
        forbidden = ("\x00", "\x01", "\x0b", "\ud800", "\udfff", "\ufffe", "\uffff")
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "invalid-name.3mf"
            for character in forbidden:
                for field in ("name", "title"):
                    name = f"Part{character}" if field == "name" else "Part"
                    params = (
                        dict(name=f"Project{character}") if field == "title" else {}
                    )
                    with self.subTest(character=repr(character), field=field):
                        with self.assertRaisesRegex(ValueError, "XML 1.0"):
                            write_orca_3mf(destination, [(name, self.mesh)], params)
                        self.assertFalse(destination.exists())

    def test_valid_xml_unicode_and_escaping_remain_supported(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "valid-name.3mf"
            write_orca_3mf(
                destination,
                [('Peça <A> & "B" Δ 🧵\t', self.mesh)],
                dict(name='Projeto <teste> & "Rosca" Δ 🧵'),
            )
            with zipfile.ZipFile(destination) as archive:
                ET.fromstring(archive.read("3D/3dmodel.model"))
                ET.fromstring(archive.read("Metadata/model_settings.config"))


class PatchInstallerTests(unittest.TestCase):
    def test_hardlinked_destinations_are_replaced_without_changing_external_files(self):
        builder = load_builder()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = root / "data"
            installed = data / "orca_plugins" / "orca_thread_generator"
            installed.mkdir(parents=True)
            outside = root / "outside"
            outside.mkdir()
            old_bundle = outside / "original.py"
            old_icon = outside / "original.svg"
            old_bundle.write_bytes(b"EXTERNAL SCRIPT MUST REMAIN UNCHANGED")
            old_icon.write_bytes(b"EXTERNAL ICON MUST REMAIN UNCHANGED")
            os.link(old_bundle, installed / "orca_thread_generator.py")
            os.link(old_icon, installed / "icon.svg")
            state = installed / ".install_state.json"
            state.write_bytes(b'{"preserve": true}')
            (installed / "old.whl").write_bytes(b"stale wheel")
            incoming = root / "incoming.py"
            icon = root / "incoming.svg"
            incoming.write_bytes(b"# new standalone plugin")
            icon.write_bytes(b"<svg/>")
            with (
                patch.object(builder, "get_orca_data_dir", return_value=data),
                patch.object(builder, "get_install_dir", return_value=installed),
                patch.object(builder, "ICON_SRC_PATH", icon),
            ):
                builder.install_plugin(incoming)
            self.assertEqual(
                old_bundle.read_bytes(), b"EXTERNAL SCRIPT MUST REMAIN UNCHANGED"
            )
            self.assertEqual(
                old_icon.read_bytes(), b"EXTERNAL ICON MUST REMAIN UNCHANGED"
            )
            self.assertEqual(
                (installed / "orca_thread_generator.py").read_bytes(),
                incoming.read_bytes(),
            )
            self.assertEqual((installed / "icon.svg").read_bytes(), icon.read_bytes())
            self.assertEqual(state.read_bytes(), b'{"preserve": true}')
            self.assertFalse((installed / "old.whl").exists())
            self.assertFalse(list(installed.glob(".orca_thread_install_*.tmp")))

    def test_external_install_directory_is_rejected_before_writing(self):
        builder = load_builder()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "incoming.py"
            source.write_bytes(b"new")
            outside = root / "outside" / "orca_thread_generator"
            with (
                patch.object(builder, "get_orca_data_dir", return_value=root / "data"),
                patch.object(builder, "get_install_dir", return_value=outside),
            ):
                with self.assertRaisesRegex(RuntimeError, "dedicated Thread"):
                    builder.install_plugin(source)
            self.assertFalse(outside.exists())

    def test_atomic_replace_failure_preserves_prior_destination_and_cleans_temp(self):
        builder = load_builder()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.py"
            source.write_bytes(b"new")
            target = root / "plugin.py"
            target.write_bytes(b"old")
            with patch.object(
                builder.os,
                "replace",
                side_effect=OSError("simulated replacement failure"),
            ):
                with self.assertRaises(OSError):
                    builder._atomic_install_file(source, target, root.resolve())
            self.assertEqual(target.read_bytes(), b"old")
            self.assertFalse(list(root.glob(".orca_thread_install_*.tmp")))

    def test_both_standalone_bundles_embed_the_complete_mit_notice(self):
        builder = load_builder()
        bundle = builder.build_bundle()
        expected = (ROOT / "LICENSE").read_text(encoding="utf-8").strip()
        for path in (bundle, builder.DIST_ANY_BUNDLE_PATH):
            source = path.read_text(encoding="utf-8")
            notice = "\n".join(
                "# " + line if line else "#" for line in expected.splitlines()
            )
            self.assertTrue(
                notice in source, f"Complete MIT notice missing from {path.name}"
            )
            self.assertLess(
                source.index("# MIT License"), source.index("from __future__ import")
            )
            compile(source, str(path), "exec")


if __name__ == "__main__":
    unittest.main()
