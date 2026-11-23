"""Native host styling and automatic-theme regressions without host RPCs."""

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from thread_studio.studio_ui import get_studio_html


@unittest.skipUnless(shutil.which("node"), "Node is needed for the embedded UI")
class HostThemeTests(unittest.TestCase):
    def run_ui(self, expression):
        script = get_studio_html().split("<script>", 1)[1].split("</script>", 1)[0]
        result = subprocess.run(
            ["node"],
            input=script + "\n" + expression,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_injected_native_background_is_detected_using_vase_luminance_rule(self):
        result = self.run_ui(
            """
            global.document = {documentElement: {}};
            let raw = '';
            global.window = {getComputedStyle: () => ({getPropertyValue: () => raw})};
            const detected = ['#fff', '#16181c', 'rgb(240, 240, 240)',
                'rgba(20, 24, 28, 1)', '', 'nonsense'].map(value => {
                    raw = value; return __threadStudio.detectInjectedOrcaTheme();
                });
            process.stdout.write(JSON.stringify(detected));
            """
        )
        self.assertEqual(result, ["light", "dark", "light", "dark", None, None])

    def test_only_nonexplicit_host_theme_adopts_native_background(self):
        result = self.run_ui(
            """
            const choose = __threadStudio.resolveStudioTheme;
            process.stdout.write(JSON.stringify([
                choose('dark', {theme_explicit:false}, 'dark', false, 'light'),
                choose('dark', {theme_explicit:true}, 'dark', false, 'light'),
                choose('dark', {}, 'dark', false, 'light'),
                choose('dark', {theme_explicit:false}, 'dark', false, null),
                choose('light', {theme_explicit:false}, 'dark', true, 'light')
            ]));
            """
        )
        self.assertEqual(result, ["light", "dark", "dark", "dark", "dark"])

    def test_late_init_cannot_replace_dirty_or_manually_selected_theme(self):
        result = self.run_ui(
            """
            global.document = {documentElement: {}};
            global.window = {getComputedStyle: () => ({getPropertyValue: () => '#fff'})};
            const current = {params:{nominal_dia:44,theme:'dark'},theme:'dark',lang:'en',
                host:{},userPresets:[],builtins:[],userOverrodeTheme:true};
            const message = {client_id:'page',request_id:0,theme:'light',lang:'pt',
                params:{nominal_dia:40,theme:'light'},host:{theme_explicit:false}};
            const dirty = __threadStudio.resolveInitialState(message,current,'page',1,0);
            const manual = __threadStudio.resolveInitialState(message,current,'page',0,0);
            current.userOverrodeTheme = false;
            const automatic = __threadStudio.resolveInitialState(message,current,'page',0,0);
            process.stdout.write(JSON.stringify([
                dirty.acceptDesign,dirty.theme,dirty.params.nominal_dia,
                manual.theme,automatic.theme]));
            """
        )
        self.assertEqual(result, [False, "dark", 44, "dark", "light"])


class HostCascadeTests(unittest.TestCase):
    def test_late_host_element_rules_have_lower_specificity_than_adapter(self):
        """Exercise source-order plus specificity for actual competing properties.

        The deliberately small matcher covers the element/attribute/class selectors
        involved here. Browser acceptance separately checks computed native styles.
        """
        css = get_studio_html().split("<style>", 1)[1].split("</style>", 1)[0]
        adapter = css.split("/* Native host compatibility.", 1)[1].split(
            "/* Thread-specific content.", 1
        )[0]
        # These late generic rules model Orca's element defaults, rather than
        # reproducing the application's source or depending on its installation.
        css = (
            adapter
            + """
        :root { --orca-accent: #e00000; }
        html, body {color:#333; background:#fff; font-size:13px; line-height:normal;}
        input, select, textarea {border:1px solid white; padding:4px 8px;}
        """
        )
        winners = {}
        for order, match in enumerate(re.finditer(r"([^{}]+)\{([^{}]*)\}", css)):
            for selector in match[1].split(","):
                selector = selector.strip()
                if selector not in {
                    "html",
                    "body",
                    "html[data-theme]",
                    "html[data-theme] body",
                    'html[data-theme="dark"]',
                    ":root",
                    "input",
                    'html[data-theme] input[type="range"].orca-slider',
                }:
                    continue
                specificity = (
                    len(re.findall(r"\[[^]]+\]|\.[\w-]+|:[\w-]+", selector)),
                    len(
                        re.findall(
                            r"(?:^|\s)(?:html|body|input)(?=\[|\.|\s|$)", selector
                        )
                    ),
                    order,
                )
                target = (
                    "slider"
                    if "input" in selector
                    else "root"
                    if selector == ":root"
                    or selector.startswith("html[")
                    and not selector.endswith("body")
                    else "body"
                )
                for declaration in match[2].split(";"):
                    if ":" not in declaration:
                        continue
                    key, value = map(str.strip, declaration.split(":", 1))
                    slot = (target, key)
                    if slot not in winners or specificity > winners[slot][0]:
                        winners[slot] = specificity, value
        for key, value in {
            "color": "var(--text-main)",
            "background": "var(--bg-app)",
            "font-size": "12.5px",
            "line-height": "1.4",
        }.items():
            self.assertEqual(winners["body", key][1], value)
        self.assertEqual(winners["root", "--orca-accent"][1], "#00a896")
        self.assertEqual(winners["slider", "border"][1], "0")
        self.assertEqual(winners["slider", "padding"][1], "0")


if __name__ == "__main__":
    unittest.main()
