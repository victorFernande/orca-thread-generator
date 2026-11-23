"""A display-name fix must retain the user's tab choice and existing grants."""
import importlib.util
import json
import os
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
spec = importlib.util.spec_from_file_location("thread_tab_builder", ROOT / "scripts/build_and_install.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class TabNameMigrationTests(unittest.TestCase):
    def test_only_the_legacy_visibility_key_changes(self):
        for visible in (False, True):
            with self.subTest(visible=visible):
                state = {"enabled": False, "permissions": {"fs_read": ["existing/*"], "threading": True},
                         "capabilities": [{"Gerador de Roscas": visible}, {"Other capability": False}],
                         "custom": "preserve"}
                before = json.dumps(state).encode()
                expected = {**state, "capabilities": [{"Thread Studio": visible}, {"Other capability": False}]}
                self.assertEqual(json.loads(builder.renamed_page_state(before)), expected)

    def test_existing_new_preference_and_ambiguous_states_are_untouched(self):
        for state in (
            {"capabilities": [{"Gerador de Roscas": True}, {"Thread Studio": False}]},
            {"capabilities": [{"Gerador de Roscas": True}, {"Gerador de Roscas": False}]},
            {"capabilities": [{"Gerador de Roscas": "true"}]},
            {"enabled": True}, [],
        ):
            before = json.dumps(state).encode()
            self.assertEqual(builder.renamed_page_state(before), before)
        self.assertEqual(builder.renamed_page_state(b"invalid JSON"), b"invalid JSON")

    def test_native_page_exposes_the_stable_studio_name(self):
        from thread_studio.plugin_main import ThreadStudioPageCapability
        self.assertEqual(ThreadStudioPageCapability().get_name(), "Thread Studio")

    def test_installer_migrates_both_state_files_and_keeps_original_backups(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            data = root / "data"
            installed = data / "orca_plugins/orca_thread_generator"
            installed.mkdir(parents=True)
            before = b'{"enabled":true,"capabilities":[{"Gerador de Roscas":false}],"permissions":{"keep":"exact"}}'
            for name in (".install_state.json", "install_state.json"):
                (installed / name).write_bytes(before)
            # Replacing a hard-linked state must not modify its external original.
            original = root / "external-state.json"
            original.write_bytes(before)
            (installed / ".install_state.json").unlink()
            os.link(original, installed / ".install_state.json")
            incoming = root / "incoming.py"
            incoming.write_bytes(b"# test plugin\n")
            with patch.object(builder, "get_orca_data_dir", return_value=data), \
                 patch.object(builder, "get_install_dir", return_value=installed), \
                 patch.object(builder, "ICON_SRC_PATH", root / "absent.svg"):
                builder.install_plugin(incoming)
                first = (installed / ".install_state.json").read_bytes()
                builder.install_plugin(incoming)
            for name in (".install_state.json", "install_state.json"):
                path = installed / name
                self.assertEqual(path.read_bytes(), first)
                self.assertEqual(json.loads(first)["capabilities"], [{"Thread Studio": False}])
                self.assertEqual(json.loads(first)["permissions"], {"keep": "exact"})
                self.assertEqual(path.with_name(path.stem + ".before-thread-studio.json").read_bytes(), before)
            self.assertEqual(original.read_bytes(), before)
            self.assertFalse(list(installed.glob(".orca_thread_state_*.tmp")))

    def test_replace_failure_keeps_previous_state_and_cleans_the_temporary_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path = root / ".install_state.json"
            path.write_bytes(b"old")
            with patch.object(builder.os, "replace", side_effect=OSError("replace failed")):
                with self.assertRaises(OSError):
                    builder._atomic_install_bytes(b"new", path, root)
            self.assertEqual(path.read_bytes(), b"old")
            self.assertFalse(list(root.glob(".orca_thread_state_*.tmp")))

    def test_linked_state_is_rejected_before_any_read_or_write(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(Path, "is_symlink", return_value=True), \
                 patch.object(Path, "read_bytes") as read:
                with self.assertRaisesRegex(RuntimeError, "linked Thread install state"):
                    builder._migrate_page_visibility(Path(directory))
                read.assert_not_called()
