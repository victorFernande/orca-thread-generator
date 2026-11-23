"""Frozen Vase visual contract; no sibling checkout or browser dependency in CI.

These declarations are the shared design primitives. Domain controls and copy may
change, while browser screenshots/computed styles remain a separate acceptance
check. The source hash records where the frozen fixture was measured.
"""
from __future__ import annotations

import copy
from html.parser import HTMLParser
import importlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unittest
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))
SCHEMA = importlib.import_module("thread_studio.schema")
UI = importlib.import_module("thread_studio.studio_ui")
PLUGIN_TITLE = "Orca Thread Studio"
CONTROL_KEYS = ('nominal_dia', 'pitch', 'thread_length', 'starts', 'wall_thickness', 'diametral_clearance', 'axial_clearance', 'inlet_diameter', 'outlet_diameter')
FAMILIES = ('container_and_lid', 'standard_bottle_cap', 'hose_vacuum_adapter', 'bolt_nut_knob')

CANONICAL_SOURCE_SHA256 = '1d644b0dda2754c641ceddad5f3e57c0d85d208a1b2c29f79e03571a599a338d'
DARK_TOKENS = {'--bg-app': '#16181c',
 '--bg-card': '#252830',
 '--bg-card-hover': '#2c303a',
 '--bg-hud': 'rgba(24,27,33,0.86)',
 '--bg-input': '#17191e',
 '--bg-panel': '#1e2026',
 '--bg-viewport-bot': '#121418',
 '--bg-viewport-top': '#232730',
 '--border-strong': '#414856',
 '--border-subtle': '#313640',
 '--font-mono': '"Cascadia Code",Consolas,"SFMono-Regular",monospace',
 '--font-sans': 'var(--orca-font,"Segoe '
                'UI",-apple-system,BlinkMacSystemFont,Roboto,Ubuntu,sans-serif)',
 '--orca-accent': '#00a896',
 '--orca-accent-border': 'rgba(0,191,165,0.48)',
 '--orca-accent-hover': '#00bfa5',
 '--orca-accent-soft': 'rgba(0,191,165,0.15)',
 '--radius-lg': '12px',
 '--radius-md': '9px',
 '--radius-sm': '6px',
 '--shadow-soft': '0 8px 24px rgba(0,0,0,0.35)',
 '--status-crit': '#ff5252',
 '--status-ok': '#00c853',
 '--status-warn': '#ffb300',
 '--text-dim': '#6e7787',
 '--text-main': '#eef2f6',
 '--text-muted': '#9aa3b2'}
LIGHT_TOKENS = {'--bg-app': '#eef2f6',
 '--bg-card': '#f5f7fa',
 '--bg-card-hover': '#eaeff5',
 '--bg-hud': 'rgba(255,255,255,0.90)',
 '--bg-input': '#ffffff',
 '--bg-panel': '#ffffff',
 '--bg-viewport-bot': '#c7d1dc',
 '--bg-viewport-top': '#dde4ec',
 '--border-strong': '#b8c3cf',
 '--border-subtle': '#d5dce4',
 '--orca-accent': '#00897b',
 '--orca-accent-border': 'rgba(0,137,123,0.45)',
 '--orca-accent-hover': '#00796b',
 '--orca-accent-soft': 'rgba(0,137,123,0.12)',
 '--shadow-soft': '0 8px 24px rgba(15,25,40,0.10)',
 '--status-crit': '#d93025',
 '--status-ok': '#1b9e4b',
 '--status-warn': '#d98200',
 '--text-dim': '#7b8696',
 '--text-main': '#1c222b',
 '--text-muted': '#556070'}
COMMON_RULES = {'#gl-canvas': {'display': 'block', 'height': '100%', 'touch-action': 'none', 'width': '100%'},
 '.action-footer': {'background': 'var(--bg-panel)',
                    'border-top': '1px solid var(--border-subtle)',
                    'display': 'flex',
                    'flex-direction': 'column',
                    'flex-shrink': '0',
                    'gap': '7px',
                    'padding': '10px'},
 '.brand-group': {'display': 'flex', 'flex': '1 1 auto', 'gap': '9px', 'min-width': '0'},
 '.brand-logo': {'background': 'linear-gradient(135deg,#00bfa5 0%,#00796b 100%)',
                 'border-radius': '7px',
                 'box-shadow': '0 2px 8px rgba(0,191,165,0.30)',
                 'height': '26px',
                 'width': '26px'},
 '.brand-title': {'font-size': '13.5px', 'font-weight': '700', 'letter-spacing': '0.2px'},
 '.btn': {'background': 'var(--bg-card)',
          'border': '1px solid var(--border-subtle)',
          'border-radius': 'var(--radius-sm)',
          'display': 'inline-flex',
          'font-size': '11.5px',
          'font-weight': '600',
          'gap': '5px',
          'padding': '5px 10px'},
 '.btn-accent': {'background': 'linear-gradient(135deg,var(--orca-accent)0%,#00897b 100%)',
                 'color': '#ffffff'},
 '.btn-hero': {'background': 'linear-gradient(135deg,#00bfa5 0%,#00897b 100%)',
               'border-radius': 'var(--radius-md)',
               'box-shadow': '0 4px 14px rgba(0,191,165,0.32)',
               'color': '#ffffff',
               'font-size': '13px',
               'font-weight': '700',
               'padding': '10px 14px',
               'width': '100%'},
 '.btn-icon': {'padding': '5px 7px'},
 '.btn-soft': {'background': 'var(--orca-accent-soft)',
               'border-color': 'var(--orca-accent-border)',
               'color': 'var(--orca-accent-hover)'},
 '.card-badge': {'background': 'var(--orca-accent-soft)',
                 'border-radius': '99px',
                 'color': 'var(--orca-accent-hover)',
                 'font-size': '10px',
                 'padding': '1px 6px'},
 '.card-head': {'align-items': 'center',
                'display': 'flex',
                'gap': '6px',
                'justify-content': 'space-between'},
 '.card-title': {'color': 'var(--text-main)',
                 'font-size': '11.5px',
                 'font-weight': '700',
                 'letter-spacing': '0.55px',
                 'text-transform': 'uppercase'},
 '.col-left': {'border-right': '1px solid var(--border-subtle)'},
 '.col-panel': {'background': 'var(--bg-panel)',
                'display': 'flex',
                'flex-direction': 'column',
                'min-height': '0',
                'overflow': 'hidden'},
 '.col-right': {'border-left': '1px solid var(--border-subtle)'},
 '.col-scroll': {'display': 'flex',
                 'flex': '1',
                 'flex-direction': 'column',
                 'gap': '10px',
                 'min-height': '0',
                 'overflow-y': 'auto',
                 'padding': '10px'},
 '.ctrl-label': {'color': 'var(--text-muted)', 'font-size': '11.3px', 'font-weight': '500'},
 '.ctrl-num': {'background': 'var(--bg-input)',
               'border-radius': '4px',
               'font-family': 'var(--font-mono)',
               'font-size': '11px',
               'padding': '2px 5px',
               'width': '58px'},
 '.ctrl-row': {'display': 'flex', 'flex-direction': 'column', 'gap': '3px'},
 '.ctrl-top': {'display': 'flex', 'gap': '6px', 'justify-content': 'space-between'},
 '.ctrl-unit': {'color': 'var(--text-dim)', 'font-size': '10px', 'min-width': '18px'},
 '.design-name-input': {'background': 'var(--bg-input)',
                        'border-radius': 'var(--radius-sm)',
                        'font-size': '12px',
                        'padding': '3px 8px',
                        'width': '165px'},
 '.dock-global-footer': {'display': 'none'},
 '.dock-tab-btn': {'border-radius': 'var(--radius-sm)',
                   'flex': '1',
                   'font-size': '11px',
                   'font-weight': '600',
                   'padding': '6px 4px'},
 '.dock-tab-btn.active': {'background': 'var(--orca-accent-soft)',
                          'border-color': 'var(--orca-accent-border)',
                          'color': 'var(--orca-accent-hover)'},
 '.dock-tabs': {'background': 'var(--bg-panel)',
                'display': 'none',
                'flex-shrink': '0',
                'gap': '4px',
                'padding': '4px 6px'},
 '.export-btn-row': {'display': 'grid', 'gap': '6px', 'grid-template-columns': '1fr 1fr auto'},
 '.header-actions': {'display': 'flex', 'flex-shrink': '0', 'gap': '5px'},
 '.preset-card': {'background': 'var(--bg-panel)',
                  'border': '1px solid var(--border-subtle)',
                  'border-radius': 'var(--radius-sm)',
                  'display': 'flex',
                  'gap': '7px',
                  'padding': '6px 7px'},
 '.presets-grid': {'display': 'grid',
                   'gap': '6px',
                   'grid-template-columns': 'repeat(2,minmax(0,1fr))',
                   'max-height': '205px',
                   'overflow-y': 'auto'},
 '.studio-card': {'background': 'var(--bg-card)',
                  'border': '1px solid var(--border-subtle)',
                  'border-radius': 'var(--radius-md)',
                  'display': 'flex',
                  'gap': '8px',
                  'padding': '10px'},
 '.studio-header': {'align-items': 'center',
                    'background': 'var(--bg-panel)',
                    'border-bottom': '1px solid var(--border-subtle)',
                    'display': 'flex',
                    'flex-shrink': '0',
                    'gap': '10px',
                    'padding': '7px 12px'},
 '.studio-shell': {'display': 'flex',
                   'flex-direction': 'column',
                   'height': '100%',
                   'width': '100%'},
 '.studio-workspace': {'display': 'grid',
                       'flex': '1',
                       'grid-template-columns': '332px minmax(340px,1fr)364px',
                       'min-height': '0',
                       'overflow': 'hidden'},
 '.toggle-switch': {'height': '18px', 'position': 'relative', 'width': '34px'},
 '.toggle-track': {'background': 'var(--border-strong)', 'border-radius': '99px'},
 '.viewport-col': {'background': 'radial-gradient(circle at 50% '
                                 '32%,var(--bg-viewport-top)0%,var(--bg-viewport-bot)100%)',
                   'display': 'flex',
                   'flex-direction': 'column',
                   'min-height': '0',
                   'min-width': '0',
                   'overflow': 'hidden',
                   'position': 'relative'},
 '.vp-glass': {'background': 'var(--bg-hud)',
               'border': '1px solid var(--border-subtle)',
               'border-radius': 'var(--radius-md)',
               'box-shadow': 'var(--shadow-soft)'},
 '[data-theme="light"] .btn-soft': {'color': 'var(--orca-accent)'},
 '[data-theme="light"] .dock-tab-btn.active': {'color': 'var(--orca-accent)'},
 'body[data-mode="dock"] .col-left': {'border': 'none', 'flex': '1', 'min-height': '0'},
 'body[data-mode="dock"] .col-right': {'border': 'none', 'flex': '1', 'min-height': '0'},
 'body[data-mode="dock"] .col-right .action-footer': {'display': 'none'},
 'body[data-mode="dock"] .design-name-input': {'width': '118px'},
 'body[data-mode="dock"] .dock-global-footer': {'display': 'flex'},
 'body[data-mode="dock"] .dock-tabs': {'display': 'flex', 'order': '0'},
 'body[data-mode="dock"] .studio-workspace': {'display': 'flex', 'flex-direction': 'column'},
 'body[data-mode="dock"] .viewport-col': {'border-bottom': '1px solid var(--border-subtle)',
                                          'flex-shrink': '0',
                                          'height': '245px',
                                          'order': '-1'},
 'html': {'background': 'var(--bg-app)',
          'color': 'var(--text-main)',
          'font-family': 'var(--font-sans)',
          'font-size': '12.5px',
          'height': '100%',
          'line-height': '1.4',
          'overflow': 'hidden',
          'width': '100%'},
 'input[type="range"].orca-slider': {'background': 'var(--border-strong)',
                                     'border-radius': '99px',
                                     'height': '5px',
                                     'width': '100%'},
 'input[type="range"].orca-slider::-webkit-slider-thumb': {'background': 'var(--orca-accent-hover)',
                                                           'border': '2px solid #ffffff',
                                                           'border-radius': '50%',
                                                           'height': '13px',
                                                           'width': '13px'}}


def normalized_css_value(value):
    return re.sub(r"\s*([,()])\s*", r"\1", " ".join(value.strip().split()))


def stylesheet_rules(css):
    """Read unconditional rules, retaining the CSS cascade for identical selectors."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    rules = {}
    cursor = 0
    while True:
        opening = css.find("{", cursor)
        if opening < 0:
            return rules
        selector = css[cursor:opening].strip()
        depth, end = 1, opening + 1
        while depth and end < len(css):
            depth += (css[end] == "{") - (css[end] == "}")
            end += 1
        if depth:
            raise AssertionError("Unbalanced CSS block")
        body = css[opening + 1:end - 1]
        cursor = end
        if selector.startswith("@"):
            continue
        declarations = {
            name: normalized_css_value(value)
            for name, value in re.findall(r"([\w-]+)\s*:\s*([^;]+)", body)
        }
        for item in selector.split(","):
            rules.setdefault(item.strip(), {}).update(declarations)


class Document(HTMLParser):
    void = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.nodes, self.stack, self.styles, self.scripts = [], [], [], []
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = dict(tag=tag, attrs=dict(attrs), parent=self.stack[-1] if self.stack else None)
        self.nodes.append(node)
        if tag not in self.void:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.nodes.append(dict(tag=tag, attrs=dict(attrs), parent=self.stack[-1] if self.stack else None))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.stack and self.stack[-1]["tag"] == "style":
            self.styles.append(data)
        elif self.stack and self.stack[-1]["tag"] == "script":
            self.scripts.append(data)

    def by_class(self, name):
        return [node for node in self.nodes if name in node["attrs"].get("class", "").split()]

    def descendants(self, ancestor):
        result = []
        for node in self.nodes:
            parent = node["parent"]
            while parent is not None:
                if parent is ancestor:
                    result.append(node)
                    break
                parent = parent["parent"]
        return result


def studio_html(mode="page", theme="dark", lang="pt", name="Visual contract"):
    params = copy.deepcopy(SCHEMA.DEFAULT_PARAMS)
    params["name"] = name
    context = dict(params=params, lang=lang, theme=theme, user_presets=[])
    return UI.get_studio_html(mode=mode, initial_context=context)


class VisualTemplateTests(unittest.TestCase):
    def test_shared_design_tokens_and_component_measurements(self):
        document = Document(studio_html())
        rules = stylesheet_rules("\n".join(document.styles))
        for selector, expected in ((":root", DARK_TOKENS), ('[data-theme="dark"]', DARK_TOKENS), ('[data-theme="light"]', LIGHT_TOKENS), *COMMON_RULES.items()):
            with self.subTest(selector=selector):
                self.assertIn(selector, rules)
                for name, value in expected.items():
                    self.assertEqual(rules[selector].get(name), value, f"{selector}: {name}")

    def test_initial_theme_language_and_mode_are_present_before_javascript(self):
        for mode in ("page", "dock"):
            for theme, lang in (("dark", "pt"), ("light", "en")):
                with self.subTest(mode=mode, theme=theme, lang=lang):
                    document = Document(studio_html(mode, theme, lang))
                    root = next(n for n in document.nodes if n["tag"] == "html")
                    body = next(n for n in document.nodes if n["tag"] == "body")
                    self.assertEqual(root["attrs"].get("data-theme"), theme)
                    self.assertEqual(root["attrs"].get("lang"), lang)
                    self.assertEqual(body["attrs"].get("data-mode"), mode)
                    self.assertEqual(body["attrs"].get("data-dock-tab"), "shape")
                    self.assertNotIn("__INITIAL_", "".join(document.scripts))

    def test_shared_shell_tabs_and_both_action_footers(self):
        for mode in ("page", "dock"):
            document = Document(studio_html(mode=mode))
            for cls in ("studio-shell", "studio-header", "brand-group", "brand-logo", "brand-title", "header-actions", "studio-workspace", "col-left", "col-right", "viewport-col", "studio-card", "dock-tabs", "design-name-input"):
                self.assertTrue(document.by_class(cls), cls)
            self.assertEqual(len(document.by_class("studio-header")), 1)
            self.assertEqual(len(document.by_class("viewport-col")), 1)
            ids = [node["attrs"]["id"] for node in document.nodes if node["attrs"].get("id")]
            self.assertEqual(len(ids), len(set(ids)), "DOM IDs must be unique")
            self.assertIn("gl-canvas", ids)
            self.assertTrue(document.by_class("printer-pill"))
            self.assertTrue({"printer-pill", "sync"} & set(ids))
            self.assertIn("presets-grid", ids)
            aliases = ({"btn-undo", "undo"}, {"btn-redo", "redo"}, {"btn-reset", "reset"}, {"btn-randomize", "randomize"}, {"btn-lang", "language", "lang"}, {"btn-theme", "theme"})
            for choices in aliases:
                self.assertTrue(set(ids) & choices, choices)
            tabs = document.by_class("dock-tab-btn")
            values = [node["attrs"].get("data-tab") for node in tabs]
            self.assertEqual(len(values), 4)
            self.assertEqual(len(set(values)), 4)
            self.assertTrue({"shape", "print", "presets"}.issubset(values))
            footers = document.by_class("action-footer")
            self.assertEqual(len(footers), 2)
            self.assertEqual(len(document.by_class("dock-global-footer")), 1)
            for footer in footers:
                actions = {n["attrs"].get("data-action") for n in document.descendants(footer)}
                self.assertTrue({"send_to_plater", "export_3mf", "export_stl", "open_folder"}.issubset(actions))

    def test_resource_controls_remain_in_the_new_template(self):
        html = studio_html()
        document = Document(html)
        source = "\n".join(document.scripts)
        controls = {node["attrs"].get("data-key") or node["attrs"].get("data-slider") for node in document.nodes}
        for key in CONTROL_KEYS:
            with self.subTest(control=key):
                self.assertTrue(key in controls or re.search(r"[\"']" + re.escape(key) + r"[\"']", source), f"Missing resource control {key}")
        for family in FAMILIES:
            self.assertIn(family, html)
        self.assertIn(PLUGIN_TITLE, html)
        self.assertNotIn("Orca Vase Studio", html)

    def test_offline_assets_and_script_safe_design_names(self):
        malicious = '</script><script id="injected">throw 1</script>\u2028\u2029'
        document = Document(studio_html(name=malicious))
        scripts = [n for n in document.nodes if n["tag"] == "script"]
        self.assertEqual(len(scripts), 1)
        self.assertFalse(any(n["attrs"].get("id") == "injected" for n in document.nodes))
        for node in document.nodes:
            if node["tag"] in {"script", "link", "img", "iframe", "source"}:
                for attr in ("src", "href"):
                    self.assertFalse(re.match(r"^(?:https?:)?//", node["attrs"].get(attr, "")), node)
        css = "\n".join(document.styles)
        script = "\n".join(document.scripts)
        self.assertNotRegex(css, r"@import|url\(\s*['\"]?(?:https?:)?//")
        self.assertNotIn("\u2028", script)
        self.assertNotIn("\u2029", script)

    @unittest.skipUnless(shutil.which("node"), "Node.js is needed for JavaScript syntax verification")
    def test_javascript_is_syntactically_valid(self):
        script = "\n".join(Document(studio_html()).scripts)
        result = subprocess.run([shutil.which("node"), "--check"], input=script, text=True, encoding="utf-8", capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(shutil.which("node"), "Node.js is needed for transform verification")
    def test_scene_bounds_include_screw_motion_handedness_and_all_calibration_rings(self):
        script = "\n".join(Document(studio_html()).scripts)
        checks = """
const assert=require('node:assert/strict'),api=globalThis.__threadStudio;
assert.ok(api && api.getSceneBounds && api.modelMatrix && api.transformPoint);
function close(actual,expected){assert.equal(actual.length,expected.length);actual.forEach((value,index)=>assert.ok(Math.abs(value-expected[index])<1e-4,JSON.stringify({actual,expected})));}
let p={...api.getState().params,module:'container_and_lid',export_target:'all',height:55,floor_thickness:2.4,lead:9,hand:'right'};
const parts=[
 {bounds:{min:[-22,-22,0],max:[22,22,55],size:[44,44,55]}},
 {bounds:{min:[-8,-3,0],max:[10,5,14.4],size:[18,8,14.4]}}
];
const view={opening:30,spin:Math.PI/2};
close(api.transformPoint([10,5,14.4],api.modelMatrix(1,parts,p,view)),[5,10,75.25]);
close(api.getSceneBounds(parts,p,view).max,[22,22,89.65]);
p.hand='left';
close(api.transformPoint([10,5,14.4],api.modelMatrix(1,parts,p,view)),[-5,-10,75.25]);
p={...p,module:'bolt_nut_knob',head_height:5,thread_length:12};
close(api.transformPoint([0,0,12],api.modelMatrix(1,parts,p,{opening:0,spin:0})),[0,0,5]);
const rings=Array.from({length:3},()=>({bounds:{min:[-5,-5,0],max:[5,5,6],size:[10,10,6]}}));
p.export_target='calibration';
close(api.getSceneBounds(rings,p,{opening:0,spin:0}).min,[-16.5,-5,0]);
close(api.getSceneBounds(rings,p,{opening:0,spin:0}).max,[16.5,5,6]);
console.log('Headless transform-aware Thread scene bounds: PASS');
"""
        result = subprocess.run(
            [shutil.which("node")], input=script + checks,
            text=True, encoding="utf-8", capture_output=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(shutil.which("node"), "Node.js is needed for loupe parity verification")
    def test_loupe_math_matches_the_exported_thread_equations(self):
        math_module = importlib.import_module("thread_studio.thread_math")
        cases = []
        for standard in ("iso_metric", "fdm_trapezoid_45", "pco1881", "mason_70", "mason_86"):
            raw = dict(module="standard_bottle_cap", standard=standard, starts=3, hand="left")
            if standard == "mason_86":
                raw.update(measurements_confirmed=True, measured_major_dia=86,
                           measured_root_dia=82, measured_pitch=6, measured_length=10)
            params = SCHEMA.normalize_params(raw)
            levels = [params["thread_length"] * index / 40 for index in range(41)]
            cases.append(dict(params=params, levels=levels))
        script = "\n".join(Document(studio_html()).scripts)
        query = "\nconst cases=" + json.dumps(cases) + ";\n" + """
console.log(JSON.stringify(cases.map(({params,levels})=>({
 male:levels.map(q=>globalThis.__threadStudio.radialProfile(q,false,params)),
 female:levels.map(q=>globalThis.__threadStudio.radialProfile(q,true,params))
}))));
"""
        result = subprocess.run(
            [shutil.which("node")], input=script + query,
            text=True, encoding="utf-8", capture_output=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        actual = json.loads(result.stdout)
        for case, output in zip(cases, actual):
            for female, key in ((False, "male"), (True, "female")):
                for level, radius in zip(case["levels"], output[key]):
                    expected = float(math_module.thread_radius(0, level, case["params"], female))
                    self.assertAlmostEqual(radius, expected, places=8)

    def test_surprise_keeps_the_family_and_never_grants_measurement_confirmation(self):
        catalog = importlib.import_module("thread_studio.presets_catalog")
        for family in FAMILIES:
            current = SCHEMA.normalize_params(dict(module=family))
            before = copy.deepcopy(current)
            for seed in (0, 1, 22, 99):
                candidate = catalog.generate_random_printable_params(seed, current)
                self.assertEqual(candidate, catalog.generate_random_printable_params(seed, current))
                self.assertEqual(candidate["module"], family)
                self.assertFalse(candidate["measurements_confirmed"])
                self.assertEqual(current, before)
        current = SCHEMA.normalize_params(dict(module="standard_bottle_cap", standard="mason_86"))
        candidate = catalog.generate_random_printable_params(12, current)
        self.assertEqual(candidate["standard"], "mason_86")
        self.assertFalse(candidate["measurements_confirmed"])
        engine = importlib.import_module("thread_studio.mesh_generator")
        with self.assertRaisesRegex(ValueError, "Mason 86"):
            engine.generate_parts(candidate)

    @unittest.skipUnless(shutil.which("node"), "Node.js is needed for request/history verification")
    def test_pending_edit_survives_toolbar_undo_and_old_requests_are_rejected(self):
        script = "\n".join(Document(studio_html()).scripts)
        checks = """
const assert=require('node:assert/strict'),api=globalThis.__threadStudio;
const current={...api.getState().params,nominal_dia:44};
const undo=api.buildMutationPayload({type:'undo'},current,1,0,'review');
assert.equal(undo.pending_params.nominal_dia,44);
current.nominal_dia=99;
assert.equal(undo.pending_params.nominal_dia,44,'Pending parameters must be cloned');
assert.equal(api.geometryRevisionIsStale({client_id:'review',request_id:1,
 client_acknowledgements:{review:2}},'review',2,0),true);
assert.equal(api.geometryRevisionIsStale({client_id:'dock',request_id:1,
 client_acknowledgements:{review:2}},'review',2,0),false);
const local={params:{...api.getState().params,nominal_dia:44,lang:'en',theme:'light'},
 lang:'en',theme:'light',host:{printer_name:'old'},userPresets:[],builtins:[]};
const initial={client_id:'review',request_id:0,params:{...api.getState().params,nominal_dia:40},
 lang:'pt',theme:'dark',host:{printer_name:'new'},user_presets:[{id:'saved'}]};
for(const acknowledged of [0,1]){
 const resolved=api.resolveInitialState(initial,local,'review',1,acknowledged);
 assert.equal(resolved.acceptDesign,false);
 assert.equal(resolved.params.nominal_dia,44);assert.equal(resolved.lang,'en');
 assert.equal(resolved.theme,'light');assert.equal(resolved.host.printer_name,'new');
 assert.equal(resolved.userPresets[0].id,'saved');
}
assert.equal(api.resolveInitialState(initial,local,'review',0,0).acceptDesign,true);
console.log(JSON.stringify(undo));
"""
        result = subprocess.run(
            [shutil.which("node")], input=script + checks,
            text=True, encoding="utf-8", capture_output=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        undo = json.loads(result.stdout)
        bridge = importlib.import_module("thread_studio.plugin_main")
        controller = bridge.ThreadStudioController()
        committed = controller.current_params
        committed["nominal_dia"] = 42
        controller.set_current_params(committed)
        with patch.object(controller, "_queue_geometry"):
            controller.handle_message(undo, lambda _message: None)
            self.assertEqual(controller.current_params["nominal_dia"], 42)
            controller.handle_message(dict(type="update", params=undo["pending_params"],
                                           request_id=1, client_id="review"), lambda _message: None)
            self.assertEqual(controller.current_params["nominal_dia"], 42)
            controller.handle_message(dict(type="redo", request_id=3, client_id="review"), lambda _message: None)
            self.assertEqual(controller.current_params["nominal_dia"], 44)

    def test_geometry_acknowledgement_cannot_describe_a_newer_design(self):
        bridge = importlib.import_module("thread_studio.plugin_main")
        controller = bridge.ThreadStudioController()
        messages = []
        controller._listeners = [messages.append]
        original_lock = controller._lock
        stage = dict(armed=False, fired=False)

        class InterleavedLock:
            def __enter__(self):
                if stage["armed"] and not stage["fired"]:
                    stage["fired"] = True
                    # Deterministically inject an update between completion and
                    # final publication, without generating either large mesh.
                    controller._revision += 1
                    controller._client_requests["review"] = 2
                    latest = controller.current_params
                    latest["nominal_dia"] = 42
                    controller._current_params = latest
                return original_lock.__enter__()

            def __exit__(self, *args):
                return original_lock.__exit__(*args)

        controller._lock = InterleavedLock()

        def compute(params):
            stage["armed"] = True
            return dict(type="geometry", params=params)

        with patch.object(controller, "_geometry_message", side_effect=compute):
            controller._queue_geometry(1, "review")
            controller._last_geometry_worker.join(5)
            self.assertFalse(controller._last_geometry_worker.is_alive())
        self.assertTrue(stage["fired"])
        for message in messages:
            if message["type"] == "geometry":
                self.assertLessEqual(message["client_acknowledgements"].get("review", -1), 1)


    @unittest.skipUnless(shutil.which("node"), "Node.js is needed for shortcut verification")
    def test_design_shortcuts_preserve_native_text_undo_and_support_control_y(self):
        script = "\n".join(Document(studio_html()).scripts)
        binding = re.search(
            r'document\s*\.\s*addEventListener\(\s*[\"\x27]keydown[\"\x27]\s*,[\s\S]*?\n\s*\}\s*\);',
            script,
        )
        self.assertIsNotNone(binding)
        fixture = """
const assert=require('node:assert/strict'),listeners={},actions=[];
const document={addEventListener:(name,handler)=>listeners[name]=handler};
const send=payload=>actions.push(payload.type);
const sendMutation=send;
const $=id=>({click(){actions.push(id==='redo'?'redo':'undo');}});
"""
        checks = """
function press(tag,key='z',shift=false,ctrl=true,meta=false){
 actions.length=0;let prevented=false;
 listeners.keydown({target:{tagName:tag,isContentEditable:false},key,
  ctrlKey:ctrl,metaKey:meta,shiftKey:shift,preventDefault(){prevented=true;}});
 return {actions:[...actions],prevented};
}
assert.deepEqual(press('INPUT'),{actions:[],prevented:false});
assert.deepEqual(press('TEXTAREA','y'),{actions:[],prevented:false});
assert.deepEqual(press('BODY'),{actions:['undo'],prevented:true});
assert.deepEqual(press('BODY','z',true),{actions:['redo'],prevented:true});
assert.deepEqual(press('BODY','y'),{actions:['redo'],prevented:true});
assert.deepEqual(press('BODY','z',false,false,true),{actions:['undo'],prevented:true});
assert.deepEqual(press('BODY','z',false,false),{actions:[],prevented:false});
"""
        result = subprocess.run(
            [shutil.which("node")], input=fixture + binding.group() + checks,
            text=True, encoding="utf-8", capture_output=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
