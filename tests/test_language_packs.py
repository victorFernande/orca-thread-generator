"""A future language is one data file, not a Python/JavaScript feature edit."""
from __future__ import annotations

import importlib.util
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from thread_studio.language_packs import load_language_packs, validate_language_pack, resolve_language
from thread_studio.locale_catalog import LANGUAGE_PACKS, SUPPORTED_LANGUAGES
from thread_studio.locale_catalog import TRANSLATIONS, translate_text


def synthetic(code="nl", name="Nederlands"):
    return {"schema_version":1,"code":code,"native_name":name,"direction":"ltr","order":7,
            "translations":{"Model Gallery":"Modellengalerij", "Save":"Opslaan"}}


def write_pack(folder, name, pack):
    path=folder/name
    path.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    return path


class LanguagePackTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('node'), 'Node.js is needed to inspect the UI vocabulary')
    def test_every_production_label_option_preset_and_tooltip_has_a_catalog_entry(self):
        import re
        from thread_studio.studio_ui import get_studio_html
        from thread_studio.presets_catalog import BUILTIN_PRESETS
        html = get_studio_html()
        script = html.split('<script>')[-1].split('</script>')[0]
        vocabulary = script[script.index('  const words ='):script.index('  function normalizeLanguage(')]
        output = subprocess.check_output(['node', '-e', vocabulary + '\nconsole.log(JSON.stringify({words,labels,options}));'], text=True)
        actual = json.loads(output)
        phrases = set(actual['words']['en'].values())
        for pair in actual['labels'].values():
            phrases.add(pair[1])
            phrases.add(re.sub(r'\s*·\s*(mm|turns)\s*$', '', pair[1]))
        for rows in actual['options'].values():
            phrases.update(row[2] for row in rows)
        phrases.update(preset['name_en'] for preset in BUILTIN_PRESETS)
        phrases.update(re.findall(r'data-locale-(?:title|aria)="([^"]+)"', html))
        for code in ('pt','en','es','it','fr','de','ja'):
            self.assertFalse(phrases - set(TRANSLATIONS[code]), (code, phrases-set(TRANSLATIONS[code])))

    def test_all_seven_catalogs_cover_the_same_vocabulary_and_core_warnings(self):
        self.assertLessEqual({'pt','en','es','it','fr','de','ja'}, set(SUPPORTED_LANGUAGES))
        for code in ('pt','en','es','it','fr','de','ja'):
            self.assertEqual(set(TRANSLATIONS[code]), set(TRANSLATIONS['en']))
            self.assertTrue(all(TRANSLATIONS[code].values()))
            self.assertEqual(translate_text('Model Gallery', code), TRANSLATIONS[code]['Model Gallery'])
            warning = 'Mason 86 experimental: confirm measured dimensions before generation'
            if code != 'en':
                self.assertNotEqual(translate_text(warning, code), warning)
                self.assertNotEqual(translate_text('Interference at this position', code), 'Interference at this position')

    def test_metadata_is_discovered_and_regional_precedence_is_dynamic(self):
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td)
            write_pack(folder,'nl.json',synthetic())
            write_pack(folder,'regional.json',synthetic('nl-NL','Nederlands (Nederland)'))
            packs, errors=load_language_packs(folder,embedded={},strict=True)
            self.assertFalse(errors)
            self.assertIn('nl',packs)
            self.assertEqual(resolve_language('NL_nl.UTF-8',packs),'nl-nl')
            self.assertEqual(resolve_language('nl_BE',packs),'nl')
            self.assertEqual(resolve_language('!unsupported!',packs),'en')
            self.assertEqual(packs['nl']['translations'].get('Missing label','Missing label'),'Missing label')
            self.assertEqual(tuple(LANGUAGE_PACKS), SUPPORTED_LANGUAGES)

    def test_bad_optional_data_does_not_disable_english_but_strict_build_rejects(self):
        malformed=[
            '{broken',
            '{"schema_version":1,"schema_version":1,"code":"nl","native_name":"Nederlands","translations":{}}',
            json.dumps({**synthetic(),"schema_version":True}),
            json.dumps({**synthetic(),"code":True}),
            json.dumps({**synthetic(),"native_name":"<script>bad</script>"}),
            json.dumps({**synthetic(),"native_name":"bad\nname"}),
            json.dumps({**synthetic(),"translations":{"Files {count}":"Bestanden"}}),
            json.dumps({**synthetic(),"translations":{"Save":"<img src=x>"}}),
            json.dumps({**synthetic(),"translations":{"":"leeg"}}),
        ]
        for content in malformed:
            with self.subTest(content=content),tempfile.TemporaryDirectory() as td:
                folder=Path(td);(folder/'bad.json').write_text(content,encoding='utf-8')
                packs,errors=load_language_packs(folder,embedded={})
                self.assertIn('en',packs);self.assertTrue(errors)
                with self.assertRaises(ValueError):load_language_packs(folder,embedded={},strict=True)
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td);write_pack(folder,'one.json',synthetic());write_pack(folder,'two.json',synthetic())
            with self.assertRaises(ValueError):load_language_packs(folder,embedded={},strict=True)
        with self.assertRaises(ValueError):
            load_language_packs(Path('missing-test-locale-folder'),embedded={'one':synthetic(),'two':synthetic()},strict=True)

    def test_sidecar_overrides_only_requested_phrases_and_preserves_placeholders(self):
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td)
            embedded={'nl':{**synthetic(), 'translations':{'Model Gallery':'Oud','Save':'Opslaan'}}}
            write_pack(folder,'nl.json',{**synthetic(),'translations':{'Model Gallery':'Nieuw'}})
            packs,_=load_language_packs(folder,embedded=embedded,strict=True)
            self.assertEqual(packs['nl']['translations'],{'Model Gallery':'Nieuw','Save':'Opslaan'})
            valid=validate_language_pack({**synthetic(),'translations':{'Files {count}: {path}':'{path} — {count} bestanden'}})
            self.assertIn('{path}',valid['translations']['Files {count}: {path}'])

    def test_added_json_is_packaged_and_recognized_by_source_both_bundles_and_wheel(self):
        with tempfile.TemporaryDirectory() as td:
            project=Path(td)/'project';project.mkdir()
            shutil.copytree(ROOT/'src',project/'src',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
            (project/'scripts').mkdir()
            shutil.copyfile(ROOT/'scripts/build_and_install.py',project/'scripts/build_and_install.py')
            for name in ('pyproject.toml','README.md','LICENSE'):shutil.copyfile(ROOT/name,project/name)
            packs=project/'src/thread_studio/locales'
            # Isolate fixture codes if a future production release already ships
            # Dutch. Never change catalogs in the developer's real checkout.
            for existing in packs.glob('*.json'):
                if json.loads(existing.read_text(encoding='utf-8')).get('code','').lower().replace('_','-') in ('nl','nl-nl'):
                    existing.unlink()
            write_pack(packs,'nl.json',synthetic())
            write_pack(packs,'nl-nl.json',synthetic('nl-nl','Nederlands (Nederland)'))
            env={k:v for k,v in os.environ.items() if k!='PYTHONPATH'}
            pages=[]
            def invoke(code,*args):
                result=subprocess.run([sys.executable,'-B','-W','error','-c',code,*map(str,args)],cwd=project,env=env,check=True,capture_output=True,text=True)
                return json.loads(result.stdout.strip().splitlines()[-1])
            inspect='''import json,sys
sys.path.insert(0,sys.argv[1])
from thread_studio.locale_catalog import SUPPORTED_LANGUAGES, normalize_language, TRANSLATIONS
from thread_studio.plugin_main import _detect_language
from thread_studio.studio_ui import get_studio_html
print(json.dumps({'codes':list(SUPPORTED_LANGUAGES),'resolved':normalize_language('nl_NL.UTF-8'),'host':_detect_language({'language':'nl_NL'}),'translated':TRANSLATIONS['nl']['Model Gallery'],'page':get_studio_html('page',{'lang':'nl'}),'dock':get_studio_html('dock',{'lang':'nl-nl'})}))
'''
            source=invoke(inspect,project/'src')
            pages.extend([{'format':'source','mode':mode,'lang':('nl' if mode=='page' else 'nl-nl'),'options':len(source['codes']),'html':source[mode]} for mode in ('page','dock')])
            self.assertEqual(source['resolved'],'nl-nl');self.assertEqual(source['host'],'nl-nl')
            self.assertIn('nl',source['codes']);self.assertEqual(source['translated'],'Modellengalerij')
            self.assertIn('Nederlands',source['page']);self.assertIn('lang="nl-nl"',source['dock'])
            subprocess.run([sys.executable,'-B','-W','error',str(project/'scripts/build_and_install.py'),'--no-install'],cwd=project,env=env,check=True,capture_output=True,text=True)
            bundle_inspect='''import importlib.util,json,sys
s=importlib.util.spec_from_file_location('thread_extra_locale',sys.argv[1]);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
print(json.dumps({'codes':list(m.SUPPORTED_LANGUAGES),'resolved':m.normalize_language('nl_NL.UTF-8'),'translated':m.TRANSLATIONS['nl']['Model Gallery'],'html':m.get_studio_html('dock',{'lang':'nl-nl'}),'page':m.get_studio_html('page',{'lang':'nl'}),'dock':m.get_studio_html('dock',{'lang':'nl-nl'})}))
'''
            for filename in ('orca_thread_generator.py','orca_thread_generator_any.py'):
                result=invoke(bundle_inspect,project/'dist'/filename)
                pages.extend([{'format':filename,'mode':mode,'lang':('nl' if mode=='page' else 'nl-nl'),'options':len(result['codes']),'html':result[mode]} for mode in ('page','dock')])
                self.assertIn('nl',result['codes']);self.assertEqual(result['resolved'],'nl-nl')
                self.assertEqual(result['translated'],'Modellengalerij');self.assertIn('lang="nl-nl"',result['html'])
            wheel=next((project/'dist').glob('*.whl'));extract=project/'wheel-extracted'
            with zipfile.ZipFile(wheel) as archive:
                self.assertIn('thread_studio/locales/nl.json',archive.namelist())
                self.assertIn('thread_studio/locales/nl-nl.json',archive.namelist())
                archive.extractall(extract)
            result=invoke(inspect,extract)
            pages.extend([{'format':'wheel','mode':mode,'lang':('nl' if mode=='page' else 'nl-nl'),'options':len(result['codes']),'html':result[mode]} for mode in ('page','dock')])
            self.assertEqual(result['resolved'],'nl-nl');self.assertIn('nl',result['codes'])
            if os.environ.get('ORCA_PLAYWRIGHT_MODULE'):
                fixtures=project/'language-fixtures.json'
                fixtures.write_text(json.dumps(pages,ensure_ascii=False),encoding='utf-8')
                browser_result=subprocess.run(['node',str(ROOT/'scripts/check_language_pack_extension.cjs'),str(fixtures)],
                               cwd=ROOT,env=os.environ.copy(),capture_output=True,text=True,timeout=120)
                self.assertEqual(browser_result.returncode,0,browser_result.stderr+browser_result.stdout)
            # Adding data next to an existing standalone file also works on restart.
            sidecar=project/'dist/locales';sidecar.mkdir()
            write_pack(sidecar,'pl.json',synthetic('pl','Polski'))
            result=invoke(bundle_inspect,project/'dist/orca_thread_generator.py')
            self.assertIn('pl',result['codes'])
            # A malformed source pack stops both release builders, not just runtime discovery.
            (packs/'broken.json').write_text('{',encoding='utf-8')
            spec=importlib.util.spec_from_file_location('thread_invalid_pack_build',project/'scripts/build_and_install.py')
            builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
            with self.assertRaises(ValueError):builder.build_bundle()
            with self.assertRaises(ValueError):builder.build_wheel()


if __name__=='__main__':unittest.main()
