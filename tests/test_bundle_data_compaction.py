"""Bundle data packing cannot rewrite executable bridge code or UI contents."""
from pathlib import Path
import ast
import importlib.util
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('data_compaction_builder',ROOT/'scripts/build_and_install.py')
builder=importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BundleDataCompactionTests(unittest.TestCase):
    def test_exact_unicode_document_and_surrounding_bridge_are_preserved(self):
        document='<!doctype html><p>日本語 · ação & <strong>AVISO</strong></p>'*120
        source='from __future__ import annotations\n_HTML = '+repr(document)+'\nclass Bridge:\n    name="unchanged"\n'
        compact=builder._compact_studio_template(source,'_HTML')
        namespace={};exec(compile(compact,'packed-fixture','exec'),namespace)
        self.assertEqual(namespace['_HTML'].encode('utf-8'),document.encode('utf-8'))
        self.assertEqual(namespace['Bridge'].name,'unchanged')
        self.assertIn('class Bridge:',compact)
        self.assertLess(len(compact.encode('utf-8')),len(source.encode('utf-8')))

    def test_missing_duplicate_or_computed_templates_fail_the_build(self):
        for source in ('OTHER="text"','_HTML="a"\n_HTML="b"','_HTML=str("data")'):
            with self.subTest(source=source),self.assertRaises(ValueError):
                builder._compact_studio_template(source,'_HTML')

    def test_real_document_round_trips_without_rewriting_other_code(self):
        package=next(p for p in (ROOT/'src').iterdir() if p.is_dir() and (p/'studio_ui.py').is_file())
        source=(package/'studio_ui.py').read_text(encoding='utf-8')
        tree=ast.parse(source)
        assignment=next(n for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.value,ast.Constant)
                        and isinstance(n.value.value,str) and n.value.value.lower().startswith('<!doctype html'))
        name=assignment.targets[0].id
        packed=ast.parse(builder._compact_studio_template(source,name))
        restored=next(n for n in packed.body if isinstance(n,ast.Assign)
                      and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))
        original=assignment.value.value
        self.assertEqual(eval(compile(ast.Expression(restored.value),'document-restore','eval'),{}),original)
        restored.value=ast.Constant(original)
        self.assertEqual(ast.dump(tree,include_attributes=False),ast.dump(packed,include_attributes=False))
