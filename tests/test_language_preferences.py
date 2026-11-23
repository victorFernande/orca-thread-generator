"""Language is presentation state: persistent, shared, and independent of meshes."""
from pathlib import Path
import json
import tempfile
import threading
import unittest
from unittest.mock import patch

import numpy as np

from thread_studio import plugin_main as plugin
from thread_studio.locale_catalog import SUPPORTED_LANGUAGES, normalize_language
from thread_studio.mesh_generator import collect_target_meshes
from thread_studio.schema import normalize_params


class LanguagePreferenceTests(unittest.TestCase):
    def test_regional_host_and_schema_follow_discovered_catalogs(self):
        for code in SUPPORTED_LANGUAGES:
            variant = code.upper() + '_XX.UTF-8'
            self.assertEqual(plugin._detect_language({'language': variant}), code)
            self.assertEqual(normalize_params({'lang': variant})['lang'], code)
        self.assertEqual(normalize_language('unsupported'), 'en')

    def test_choice_is_broadcast_persisted_and_never_queues_mesh_or_history(self):
        with tempfile.TemporaryDirectory() as td, patch.object(plugin, '_resolve_storage_dir', return_value=Path(td)):
            c = plugin.ThreadStudioController()
            c.build_initial_context()
            page, dock = [], []
            c._listeners = [page.append, dock.append]
            before = c.current_params
            with patch.object(c, '_queue_geometry') as queue:
                c.handle_message({'type': 'set_language', 'lang': 'it_IT'}, page.append)
                queue.assert_not_called()
            self.assertEqual(c.current_params, dict(before, lang='it'))
            self.assertFalse(c._undo)
            self.assertEqual(page[-1], dock[-1])
            self.assertEqual(json.loads((Path(td)/'ui_preferences.json').read_text())['lang'], 'it')
            fresh = plugin.ThreadStudioController()
            self.assertEqual(fresh.build_initial_context('dock')['lang'], 'it')
            with patch.object(c, 'read_host_context', return_value={'lang':'en','theme':'dark'}):
                c.handle_message({'type':'sync_printer'}, page.append)
                self.assertEqual(c.build_initial_context()['lang'], 'it')
            self.assertEqual(list(Path(td).glob('*.tmp')), [])

    def test_old_geometry_cannot_overwrite_a_new_language_choice(self):
        with tempfile.TemporaryDirectory() as td, patch.object(plugin, '_resolve_storage_dir', return_value=Path(td)):
            c = plugin.ThreadStudioController()
            c.build_initial_context()
            started, release = threading.Event(), threading.Event()
            out = []
            def geometry(p):
                started.set()
                self.assertTrue(release.wait(5))
                return {'type': 'geometry', 'params': p}
            c._listeners = [out.append]
            with patch.object(c, '_geometry_message', side_effect=geometry):
                c._queue_geometry()
                self.assertTrue(started.wait(5))
                c.handle_message({'type':'set_language','lang':'ja'}, out.append)
                release.set()
                c._last_geometry_worker.join(5)
            self.assertFalse(c._last_geometry_worker.is_alive())
            result = next(m for m in out if m['type']=='geometry')
            self.assertEqual(result['params']['lang'], 'ja')

    def test_reset_undo_and_redo_keep_the_manual_language(self):
        with tempfile.TemporaryDirectory() as td, patch.object(plugin, '_resolve_storage_dir', return_value=Path(td)):
            c=plugin.ThreadStudioController()
            c.build_initial_context()
            c.set_current_params(dict(c.current_params,height=70))
            c.handle_message({'type':'set_language','lang':'de'}, lambda m:None)
            with patch.object(c, '_queue_geometry'):
                for action in ('undo','redo','reset'):
                    c.handle_message({'type':action}, lambda m:None)
                    self.assertEqual(c.current_params['lang'],'de')

    def test_corrupt_preference_file_falls_back_to_host(self):
        with tempfile.TemporaryDirectory() as td, patch.object(plugin, '_resolve_storage_dir', return_value=Path(td)):
            path=Path(td)/'ui_preferences.json'
            for content in ('{broken', '[]', '{"lang": true}'):
                path.write_text(content)
                c=plugin.ThreadStudioController()
                with patch.object(c,'read_host_context',return_value={'lang':'fr','theme':'dark'}):
                    self.assertEqual(c.build_initial_context()['lang'],'fr')

    def test_late_language_request_cannot_replace_or_persist_an_older_choice(self):
        with tempfile.TemporaryDirectory() as td, patch.object(plugin, '_resolve_storage_dir', return_value=Path(td)):
            c=plugin.ThreadStudioController()
            out=[]
            c.handle_message({'type':'set_language','lang':'ja','client_id':'page','language_request_id':2},out.append)
            c.handle_message({'type':'set_language','lang':'pt','client_id':'page','language_request_id':1},out.append)
            self.assertEqual(c.current_params['lang'],'ja')
            self.assertEqual(len(out),1)
            self.assertEqual(json.loads((Path(td)/'ui_preferences.json').read_text())['lang'],'ja')

    def test_language_does_not_change_actual_vertices_or_triangles(self):
        reference = collect_target_meshes({'resolution':48})
        for code in SUPPORTED_LANGUAGES:
            actual = collect_target_meshes({'lang':code,'resolution':48})
            self.assertEqual([n for n,_ in actual],[n for n,_ in reference])
            for (_,first),(_,second) in zip(reference, actual, strict=True):
                np.testing.assert_array_equal(first.vertices,second.vertices)
                np.testing.assert_array_equal(first.triangles,second.triangles)


if __name__=='__main__':
    unittest.main()
