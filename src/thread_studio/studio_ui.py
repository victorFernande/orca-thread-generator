"""Offline Thread Studio on the canonical Orca Vase Studio interface template.

Common CSS, layout, controls and studio materials derive from Orca Vase Studio
under MIT; models displayed here are the native Thread Studio mesh arrays.
"""

from __future__ import annotations
import copy
import json
from html import escape
from .locale_catalog import LANGUAGE_METADATA, TRANSLATIONS, normalize_language
from .schema import DEFAULT_PARAMS, normalize_params
from .presets_catalog import BUILTIN_PRESETS


def get_studio_html(mode="page", initial_context=None):
    context = copy.deepcopy(initial_context or {})
    context["params"] = normalize_params(context.get("params", DEFAULT_PARAMS))
    context.setdefault("builtin_presets", BUILTIN_PRESETS)
    context.setdefault("user_presets", [])
    context["mode"] = "dock" if mode == "dock" else "page"
    context["lang"] = normalize_language(context.get("lang", context["params"]["lang"]))
    context["languages"] = LANGUAGE_METADATA
    context["translations"] = TRANSLATIONS
    context["theme"] = (
        "light"
        if context.get("theme", context["params"]["theme"]) == "light"
        else "dark"
    )
    context["params"]["lang"] = context["lang"]
    context["params"]["theme"] = context["theme"]
    payload = (
        json.dumps(context, ensure_ascii=False, separators=(",", ":"))
        .replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    return (
        _HTML.replace("__THREAD_BOOT_JSON__", payload)
        .replace("__THREAD_LANGUAGE_OPTIONS__", "".join(
            f'<option value="{escape(m["code"], quote=True)}">{escape(m["native_name"])}</option>'
            for m in LANGUAGE_METADATA))
        .replace("__INITIAL_LANG__", context["lang"])
        .replace("__INITIAL_THEME__", context["theme"])
        .replace("__INITIAL_MODE__", context["mode"])
    )


_HTML = r"""<!DOCTYPE html><html lang="__INITIAL_LANG__" data-theme="__INITIAL_THEME__"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Orca Thread Studio</title><style>
:root,
[data-theme="dark"] {
  --bg-app: #16181c;
  --bg-panel: #1e2026;
  --bg-card: #252830;
  --bg-card-hover: #2c303a;
  --bg-input: #17191e;
  --bg-viewport-top: #232730;
  --bg-viewport-bot: #121418;
  --bg-hud: rgba(24, 27, 33, 0.86);
  --border-subtle: #313640;
  --border-strong: #414856;
  --text-main: #eef2f6;
  --text-muted: #9aa3b2;
  --text-dim: #6e7787;
  --orca-accent: #00a896;
  --orca-accent-hover: #00bfa5;
  --orca-accent-soft: rgba(0, 191, 165, 0.15);
  --orca-accent-border: rgba(0, 191, 165, 0.48);
  --status-ok: #00c853;
  --status-warn: #ffb300;
  --status-crit: #ff5252;
  --shadow-soft: 0 8px 24px rgba(0, 0, 0, 0.35);
  --radius-sm: 6px;
  --radius-md: 9px;
  --radius-lg: 12px;
  --font-sans: var(--orca-font, "Segoe UI", -apple-system, BlinkMacSystemFont, Roboto, Ubuntu, sans-serif);
  --font-mono: "Cascadia Code", Consolas, "SFMono-Regular", monospace;
}

[data-theme="light"] {
  --bg-app: #eef2f6;
  --bg-panel: #ffffff;
  --bg-card: #f5f7fa;
  --bg-card-hover: #eaeff5;
  --bg-input: #ffffff;
  --bg-viewport-top: #dde4ec;
  --bg-viewport-bot: #c7d1dc;
  --bg-hud: rgba(255, 255, 255, 0.90);
  --border-subtle: #d5dce4;
  --border-strong: #b8c3cf;
  --text-main: #1c222b;
  --text-muted: #556070;
  --text-dim: #7b8696;
  --orca-accent: #00897b;
  --orca-accent-hover: #00796b;
  --orca-accent-soft: rgba(0, 137, 123, 0.12);
  --orca-accent-border: rgba(0, 137, 123, 0.45);
  --status-ok: #1b9e4b;
  --status-warn: #d98200;
  --status-crit: #d93025;
  --shadow-soft: 0 8px 24px rgba(15, 25, 40, 0.10);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--bg-app);
  color: var(--text-main);
  font-family: var(--font-sans);
  font-size: 12.5px;
  line-height: 1.4;
  user-select: none;
  -webkit-font-smoothing: antialiased;
}

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: 99px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--orca-accent);
}

button, input, select {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
}

.studio-shell {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}

/* Header Bar */
.studio-header {
  display: flex;
  min-height: 43px;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 7px 12px;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
  z-index: 20;
}

.brand-group {
  display: flex;
  align-items: center;
  gap: 9px;
  min-width: 0;
  flex: 1 1 auto;
}

.brand-logo {
  width: 26px;
  height: 26px;
  border-radius: 7px;
  background: linear-gradient(135deg, #00bfa5 0%, #00796b 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(0, 191, 165, 0.30);
}

.brand-titles {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.brand-name-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.brand-title {
  font-weight: 700;
  font-size: 13.5px;
  letter-spacing: 0.2px;
  white-space: nowrap;
}

.design-name-input {
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 3px 8px;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-main);
  width: 165px;
  transition: border-color 0.15s;
}
.design-name-input:focus {
  outline: none;
  border-color: var(--orca-accent);
}

.printer-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 11px;
  border-radius: 99px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  font-size: 11px;
  white-space: nowrap;
  max-width: min(560px, 56vw);
  min-width: 0;
  flex: 0 1 auto;
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s, color 0.15s;
}
.printer-pill:hover {
  border-color: var(--orca-accent-border);
  background: var(--bg-card-hover);
  color: var(--text-main);
}
.printer-pill:active {
  transform: translateY(1px);
}

.printer-pill-text {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-width: 0;
  overflow: hidden;
}

.printer-pill-name {
  min-width: 0;
  max-width: 260px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 600;
  color: var(--text-main);
}

.printer-pill-specs {
  flex-shrink: 0;
  white-space: nowrap;
  color: var(--text-muted);
  font-family: var(--font-mono);
  font-size: 10.6px;
}

.printer-pill-sync {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 11.5px;
  line-height: 1;
  color: var(--orca-accent-hover);
  margin-left: 1px;
  transition: transform 0.38s ease;
}
[data-theme="light"] .printer-pill-sync {
  color: var(--orca-accent);
}
.printer-pill.syncing .printer-pill-sync {
  transform: rotate(360deg);
}

.printer-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--orca-accent-hover);
  flex-shrink: 0;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-shrink: 0;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  padding: 5px 10px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-card);
  color: var(--text-main);
  font-weight: 600;
  font-size: 11.5px;
  cursor: pointer;
  transition: background 0.14s, border-color 0.14s, transform 0.08s;
  white-space: nowrap;
}
.btn:hover:not(:disabled) {
  background: var(--bg-card-hover);
  border-color: var(--border-strong);
}
.btn:active:not(:disabled) {
  transform: translateY(1px);
}
.btn:disabled {
  opacity: 0.42;
  cursor: not-allowed;
}

.btn-icon {
  padding: 5px 7px;
}

.btn-accent {
  background: linear-gradient(135deg, var(--orca-accent) 0%, #00897b 100%);
  border-color: transparent;
  color: #ffffff;
}
.btn-accent:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--orca-accent-hover) 0%, var(--orca-accent) 100%);
  border-color: transparent;
}

.btn-soft {
  background: var(--orca-accent-soft);
  border-color: var(--orca-accent-border);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .btn-soft {
  color: var(--orca-accent);
}
.btn-soft:hover:not(:disabled) {
  background: var(--orca-accent);
  color: #ffffff;
}

/* Main Workspace Grid */
.studio-workspace {
  flex: 1;
  min-height: 0;
  display: grid;
  grid-template-columns: 332px minmax(340px, 1fr) 364px;
  overflow: hidden;
}

.col-panel {
  display: flex;
  flex-direction: column;
  min-height: 0;
  background: var(--bg-panel);
  overflow: hidden;
}
.col-left {
  border-right: 1px solid var(--border-subtle);
}
.col-right {
  border-left: 1px solid var(--border-subtle);
}

.col-scroll {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Dock Mode Navigation Tabs (hidden in wide page mode) */
.dock-tabs {
  display: none;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border-subtle);
  padding: 4px 6px;
  gap: 4px;
  flex-shrink: 0;
}

.dock-tab-btn {
  flex: 1;
  padding: 6px 4px;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: all 0.14s;
}
.dock-tab-btn:hover {
  color: var(--text-main);
  background: var(--bg-card);
}
.dock-tab-btn.active {
  background: var(--orca-accent-soft);
  border-color: var(--orca-accent-border);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .dock-tab-btn.active {
  color: var(--orca-accent);
}

/* Cards & Sections */
.studio-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
}

.card-title {
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.55px;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-badge {
  font-size: 10px;
  font-weight: 600;
  padding: 1px 6px;
  border-radius: 99px;
  background: var(--orca-accent-soft);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .card-badge {
  color: var(--orca-accent);
}

/* Presets Grid */
.preset-filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.filter-chip {
  padding: 3px 7px;
  font-size: 10.5px;
  font-weight: 600;
  border-radius: 99px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-input);
  color: var(--text-muted);
  cursor: pointer;
}
.filter-chip.active {
  background: var(--orca-accent);
  border-color: var(--orca-accent);
  color: #ffffff;
}

.presets-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 6px;
  max-height: 205px;
  overflow-y: auto;
  padding-right: 2px;
}

.preset-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 6px 7px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-panel);
  cursor: pointer;
  transition: border-color 0.14s, background 0.14s;
  text-align: left;
}
.preset-card:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-strong);
}
.preset-card.active {
  border-color: var(--orca-accent-hover);
  background: var(--orca-accent-soft);
}

.preset-thumb {
  width: 30px;
  height: 36px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.preset-meta {
  min-width: 0;
  flex: 1;
}

.preset-name {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-main);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.preset-sub {
  font-size: 9.8px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.preset-del-btn {
  position: absolute;
  top: 3px;
  right: 3px;
  width: 17px;
  height: 17px;
  border-radius: 4px;
  border: none;
  background: rgba(255, 82, 82, 0.16);
  color: var(--status-crit);
  font-size: 11px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
.preset-del-btn:hover {
  background: var(--status-crit);
  color: #ffffff;
}

.save-preset-bar {
  display: none;
  gap: 5px;
  align-items: center;
  padding-top: 4px;
  border-top: 1px dashed var(--border-subtle);
}
.save-preset-bar.open {
  display: flex;
}
.save-preset-input {
  flex: 1;
  min-width: 0;
  background: var(--bg-input);
  border: 1px solid var(--orca-accent-border);
  border-radius: var(--radius-sm);
  padding: 4px 7px;
  font-size: 11.5px;
}

/* Segmented Mode Switch */
.seg-group {
  display: flex;
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 2px;
  gap: 2px;
}

.seg-btn {
  flex: 1;
  padding: 5px 6px;
  border: none;
  border-radius: 4px;
  background: transparent;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.14s;
}
.seg-btn.active {
  background: var(--orca-accent);
  color: #ffffff;
}

/* 2D Curve Canvas Box */
.curve-editor-wrap {
  position: relative;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-input);
  overflow: hidden;
}

#curve-canvas {
  display: block;
  width: 100%;
  height: 220px;
  cursor: crosshair;
  touch-action: none;
}

.curve-overlay-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 8px;
  background: var(--bg-panel);
  border-top: 1px solid var(--border-subtle);
  font-size: 10.5px;
  color: var(--text-muted);
}

.curve-coord-readout {
  font-family: var(--font-mono);
  font-size: 10.5px;
  color: var(--orca-accent-hover);
}
[data-theme="light"] .curve-coord-readout {
  color: var(--orca-accent);
}

.curve-hint {
  font-size: 10.2px;
  color: var(--text-dim);
}

/* Slider Controls */
.ctrl-row {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.ctrl-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
}

.ctrl-label {
  font-size: 11.3px;
  color: var(--text-muted);
  font-weight: 500;
}

.ctrl-val-wrap {
  display: flex;
  align-items: center;
  gap: 3px;
}

.ctrl-num {
  width: 58px;
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: 4px;
  padding: 2px 5px;
  text-align: right;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-main);
}
.ctrl-num:focus {
  outline: none;
  border-color: var(--orca-accent);
}

.ctrl-unit {
  font-size: 10px;
  color: var(--text-dim);
  min-width: 18px;
}

input[type="range"].orca-slider {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 5px;
  border-radius: 99px;
  background: var(--border-strong);
  outline: none;
  cursor: pointer;
}
input[type="range"].orca-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 13px;
  height: 13px;
  border-radius: 50%;
  background: var(--orca-accent-hover);
  border: 2px solid #ffffff;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.4);
  cursor: grab;
  transition: transform 0.1s;
}
input[type="range"].orca-slider::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

/* Toggle Switch */
.switch-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 34px;
  height: 18px;
  flex-shrink: 0;
}
.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}
.toggle-track {
  position: absolute;
  inset: 0;
  background: var(--border-strong);
  border-radius: 99px;
  cursor: pointer;
  transition: background 0.18s;
}
.toggle-track::before {
  content: "";
  position: absolute;
  width: 14px;
  height: 14px;
  left: 2px;
  top: 2px;
  border-radius: 50%;
  background: #ffffff;
  transition: transform 0.18s;
}
.toggle-switch input:checked + .toggle-track {
  background: var(--orca-accent);
}
.toggle-switch input:checked + .toggle-track::before {
  transform: translateX(16px);
}

/* Texture Accordion Layer Cards */
.tex-card {
  background: var(--bg-panel);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  overflow: hidden;
  transition: border-color 0.15s;
}
.tex-card.enabled {
  border-color: var(--orca-accent-border);
}

.tex-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 7px 9px;
  background: var(--bg-card);
  cursor: pointer;
}
.tex-card.enabled .tex-head {
  background: var(--orca-accent-soft);
}

.tex-title-wrap {
  display: flex;
  align-items: center;
  gap: 7px;
  font-weight: 600;
  font-size: 12px;
}

.tex-chevron {
  font-size: 10px;
  color: var(--text-muted);
  transition: transform 0.15s;
}
.tex-card.expanded .tex-chevron {
  transform: rotate(90deg);
}

.tex-body {
  display: none;
  padding: 8px 9px 10px;
  border-top: 1px solid var(--border-subtle);
  flex-direction: column;
  gap: 7px;
}
.tex-card.expanded .tex-body {
  display: flex;
}

/* Center 3D Viewport */
.viewport-col {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  min-height: 0;
  background: radial-gradient(circle at 50% 32%, var(--bg-viewport-top) 0%, var(--bg-viewport-bot) 100%);
  overflow: hidden;
}

#gl-canvas {
  width: 100%;
  height: 100%;
  display: block;
  touch-action: none;
  cursor: grab;
}
#gl-canvas:active {
  cursor: grabbing;
}

#vp-caliper-canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
  pointer-events: none;
  z-index: 5;
}

/* Wall Thickness Quick Presets & Perimeter Hint */
.wall-preset-row {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-top: 1px;
}

.wall-chip {
  flex: 1;
  min-width: 48px;
  padding: 3px 5px;
  border-radius: 5px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-input);
  color: var(--text-muted);
  font-family: var(--font-mono);
  font-size: 10.2px;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: all 0.14s;
}
.wall-chip:hover {
  color: var(--text-main);
  border-color: var(--border-strong);
  background: var(--bg-card-hover);
}
.wall-chip.active {
  background: var(--orca-accent-soft);
  border-color: var(--orca-accent-hover);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .wall-chip.active {
  color: var(--orca-accent);
  border-color: var(--orca-accent);
}

.wall-perim-hint {
  font-size: 10.4px;
  color: var(--orca-accent-hover);
  font-family: var(--font-mono);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  padding: 3px 7px;
  border-radius: 5px;
  background: var(--orca-accent-soft);
  border: 1px solid var(--orca-accent-border);
}
[data-theme="light"] .wall-perim-hint {
  color: var(--orca-accent);
}

/* Floating Viewport Overlays */
.vp-toolbar-left {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 5px;
  max-width: calc(100% - 252px);
  z-index: 10;
}

.vp-glass {
  background: var(--bg-hud);
  backdrop-filter: blur(8px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-soft);
}

.vp-select {
  background: var(--bg-hud);
  color: var(--text-main);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 5px 8px;
  font-size: 11.5px;
  font-weight: 600;
  cursor: pointer;
}

.vp-chip {
  padding: 5px 8px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-hud);
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.vp-chip:hover {
  color: var(--text-main);
  border-color: var(--border-strong);
}
.vp-chip.active {
  background: var(--orca-accent);
  border-color: var(--orca-accent);
  color: #ffffff;
}
.vp-chip-xray {
  border-color: var(--orca-accent-border);
  color: var(--text-main);
}
.vp-chip-xray.active {
  background: linear-gradient(135deg, #00bfa5 0%, #ff8f00 130%);
  border-color: transparent;
  color: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 191, 165, 0.35);
}

.spiral-mode-banner {
  display: none;
  position: absolute;
  top: 48px;
  left: 10px;
  max-width: calc(100% - 256px);
  padding: 5px 10px;
  font-size: 10.6px;
  font-weight: 600;
  line-height: 1.3;
  z-index: 12;
  border-left: 3px solid var(--orca-accent-hover);
  color: var(--text-main);
  pointer-events: none;
}
.spiral-mode-banner.visible {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.spiral-mode-banner.warn {
  border-left-color: var(--status-warn);
  background: rgba(45, 34, 14, 0.90);
}
[data-theme="light"] .spiral-mode-banner.warn {
  background: rgba(255, 245, 224, 0.94);
}

.vp-cam-bar {
  position: absolute;
  bottom: 56px;
  left: 10px;
  display: flex;
  gap: 4px;
  z-index: 10;
}

.vp-cut-bar {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 6px 10px;
  z-index: 10;
}

.vp-cut-modes {
  display: inline-flex;
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 2px;
  gap: 2px;
  flex-shrink: 0;
}

.vp-cut-mode-btn {
  padding: 3px 7px;
  border: none;
  border-radius: 4px;
  background: transparent;
  color: var(--text-muted);
  font-size: 10.5px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.14s;
}
.vp-cut-mode-btn:hover {
  color: var(--text-main);
}
.vp-cut-mode-btn.active {
  background: var(--orca-accent);
  color: #ffffff;
}

.vp-cut-label {
  font-size: 11px;
  font-weight: 600;
  white-space: nowrap;
  color: var(--text-muted);
}

/* Printability HUD */
.vp-hud-right {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 236px;
  padding: 9px 11px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  z-index: 10;
}

.hud-title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 10.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-muted);
}

.hud-status-pill {
  padding: 1px 7px;
  border-radius: 99px;
  font-size: 10px;
  font-weight: 700;
}
.hud-status-pill.ok {
  background: rgba(0, 200, 83, 0.18);
  color: var(--status-ok);
}
.hud-status-pill.warn {
  background: rgba(255, 179, 0, 0.20);
  color: var(--status-warn);
}
.hud-status-pill.crit {
  background: rgba(255, 82, 82, 0.22);
  color: var(--status-crit);
}

.hud-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px 8px;
}

.hud-metric {
  display: flex;
  flex-direction: column;
}
.hud-metric-k {
  font-size: 9.8px;
  color: var(--text-dim);
}
.hud-metric-v {
  font-family: var(--font-mono);
  font-size: 11.2px;
  font-weight: 600;
  color: var(--text-main);
}

.hud-warnings {
  display: flex;
  flex-direction: column;
  gap: 3px;
  max-height: 92px;
  overflow-y: auto;
}

.hud-warn-item {
  font-size: 10.2px;
  padding: 3px 6px;
  border-radius: 4px;
  background: rgba(255, 179, 0, 0.13);
  border-left: 2px solid var(--status-warn);
  color: var(--text-main);
}
.hud-warn-item.crit {
  background: rgba(255, 82, 82, 0.15);
  border-left-color: var(--status-crit);
}

.heatmap-legend {
  display: none;
  align-items: center;
  gap: 6px;
  font-size: 10px;
  padding-top: 4px;
  border-top: 1px solid var(--border-subtle);
  color: var(--text-muted);
}
.heatmap-legend.visible {
  display: flex;
}
.legend-swatch {
  width: 9px;
  height: 9px;
  border-radius: 2px;
  display: inline-block;
}

.bed-alert-banner {
  display: none;
  position: absolute;
  top: 52px;
  left: 50%;
  transform: translateX(-50%);
  padding: 6px 12px 6px 14px;
  border-radius: 99px;
  background: rgba(213, 0, 0, 0.90);
  color: #ffffff;
  font-weight: 700;
  font-size: 11.5px;
  box-shadow: 0 4px 16px rgba(213, 0, 0, 0.45);
  z-index: 15;
  pointer-events: auto;
  white-space: nowrap;
}
.bed-alert-banner.visible {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.bed-fit-btn {
  padding: 2px 9px;
  border-radius: 99px;
  border: 1px solid rgba(255, 255, 255, 0.65);
  background: rgba(255, 255, 255, 0.18);
  color: #ffffff;
  font-size: 10.5px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.14s;
}
.bed-fit-btn:hover {
  background: rgba(255, 255, 255, 0.32);
}

/* Right Action Footer */
.action-footer {
  padding: 10px;
  background: var(--bg-panel);
  border-top: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  gap: 7px;
  flex-shrink: 0;
}

.btn-hero {
  width: 100%;
  padding: 10px 14px;
  font-size: 13px;
  font-weight: 700;
  border-radius: var(--radius-md);
  background: linear-gradient(135deg, #00bfa5 0%, #00897b 100%);
  color: #ffffff;
  border: none;
  box-shadow: 0 4px 14px rgba(0, 191, 165, 0.32);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: filter 0.15s, transform 0.08s;
}
.btn-hero:hover:not(:disabled) {
  filter: brightness(1.07);
}
.btn-hero:active:not(:disabled) {
  transform: translateY(1px);
}
.btn-hero:disabled {
  opacity: 0.55;
  cursor: wait;
}

.export-btn-row {
  display: grid;
  grid-template-columns: 1fr 1fr auto;
  gap: 6px;
}

.helper-note {
  font-size: 10.5px;
  color: var(--text-muted);
  background: var(--bg-input);
  border-left: 2px solid var(--orca-accent);
  padding: 5px 7px;
  border-radius: 0 4px 4px 0;
}

.helper-note.warn {
  border-left-color: var(--status-warn);
  background: rgba(255, 179, 0, 0.10);
}

/* Toast Notification */
.toast-banner {
  position: fixed;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  opacity: 0;
  pointer-events: none;
  padding: 8px 16px;
  border-radius: var(--radius-md);
  background: var(--bg-card);
  border: 1px solid var(--orca-accent);
  color: var(--text-main);
  font-size: 12px;
  font-weight: 600;
  box-shadow: var(--shadow-soft);
  transition: opacity 0.2s, transform 0.2s;
  z-index: 999;
  max-width: 90vw;
}
.toast-banner.visible {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
.toast-banner.error {
  border-color: var(--status-crit);
}

/* ============================================================================
   COMPACT SIDE-DOCK MODE (`data-mode="dock"` or narrow viewports <= 960px)
   ============================================================================ */
body[data-mode="dock"] .printer-pill,
body[data-mode="dock"] .brand-title {
  display: none;
}

body[data-mode="dock"] .design-name-input {
  width: 118px;
}

body[data-mode="dock"] .studio-workspace {
  display: flex;
  flex-direction: column;
}

body[data-mode="dock"] .viewport-col {
  order: -1;
  height: 245px;
  flex-shrink: 0;
  border-bottom: 1px solid var(--border-subtle);
}

body[data-mode="dock"] .vp-hud-right {
  width: 172px;
  padding: 5px 7px;
  gap: 3px;
}
body[data-mode="dock"] .hud-warnings,
body[data-mode="dock"] .spiral-mode-banner {
  display: none;
}
body[data-mode="dock"] .vp-cam-bar {
  display: none;
}
body[data-mode="dock"] .vp-cut-bar {
  padding: 4px 6px;
  bottom: 6px;
  gap: 4px;
}
body[data-mode="dock"] .vp-cut-mode-btn {
  padding: 2px 5px;
  font-size: 9.8px;
}

body[data-mode="dock"] .dock-tabs {
  display: flex;
  order: 0;
}

body[data-mode="dock"] .col-left,
body[data-mode="dock"] .col-right {
  border: none;
  flex: 1;
  min-height: 0;
}

body[data-mode="dock"] .col-right .action-footer {
  display: none;
}

.dock-global-footer {
  display: none;
}
body[data-mode="dock"] .dock-global-footer {
  display: flex;
}

body[data-mode="dock"][data-dock-tab="shape"] .col-right {
  display: none;
}
body[data-mode="dock"][data-dock-tab="shape"] #card-presets {
  display: none;
}

body[data-mode="dock"][data-dock-tab="presets"] .col-right {
  display: none;
}
body[data-mode="dock"][data-dock-tab="presets"] #card-silhouette,
body[data-mode="dock"][data-dock-tab="presets"] #card-resolution {
  display: none;
}
body[data-mode="dock"][data-dock-tab="presets"] .presets-grid {
  max-height: none;
}

body[data-mode="dock"][data-dock-tab="textures"] .col-left {
  display: none;
}
body[data-mode="dock"][data-dock-tab="textures"] #card-print-mode,
body[data-mode="dock"][data-dock-tab="textures"] #card-gardening {
  display: none;
}

body[data-mode="dock"][data-dock-tab="print"] .col-left {
  display: none;
}
body[data-mode="dock"][data-dock-tab="print"] #card-envelope,
body[data-mode="dock"][data-dock-tab="print"] #card-textures {
  display: none;
}

@media (max-width: 960px) {
  .printer-pill {
    display: none;
  }
  .studio-workspace {
    grid-template-columns: 280px minmax(260px, 1fr) 300px;
  }
}

/* Native host compatibility. The canonical template above stays unchanged.
   Orca appends generic element defaults after this page's styles. */
html[data-theme],
html[data-theme] body {
  background: var(--bg-app);
  color: var(--text-main);
  font-family: var(--font-sans);
  font-size: 12.5px;
  line-height: 1.4;
}
html[data-theme="dark"] { --orca-accent: #00a896; }
html[data-theme="light"] { --orca-accent: #00897b; }
html[data-theme] input[type="range"].orca-slider {
  border: 0;
  padding: 0;
}
html[data-theme] .save-preset-input { color: var(--text-main); }
html[data-theme] ::-webkit-scrollbar { width: 6px; height: 6px; }
html[data-theme] ::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: 99px;
}
html[data-theme] ::-webkit-scrollbar-thumb:hover { background: var(--orca-accent); }

/* Thread-specific content. Common studio rules above are the canonical template. */
[hidden]{display:none!important}.thread-select{width:100%}.thread-dimension-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}.thread-loupe{height:154px;flex-shrink:0;border-top:1px solid var(--border-subtle);padding:9px 12px;background:var(--bg-panel);display:flex;flex-direction:column;gap:4px}.thread-loupe canvas{height:94px;width:100%;min-height:0;flex:1}.thread-loupe-legend{display:flex;gap:14px;align-items:center;font:10px var(--font-mono);color:var(--text-muted)}.thread-loupe-legend>span{display:inline-flex;align-items:center;gap:5px}.thread-key{width:7px;height:7px;border-radius:50%;display:inline-block}.thread-key.male{background:#00bfa5}.thread-key.female{background:#ffb74d}.viewport-col>#gl-canvas{height:calc(100% - 154px);flex:1;min-height:0}.viewport-col>#vp-caliper-canvas{height:calc(100% - 154px)}.viewport-col .vp-cam-bar{bottom:210px}.viewport-col .vp-cut-bar{bottom:164px}.thread-assembly-bar{position:absolute;left:10px;bottom:250px;display:flex;gap:7px;align-items:center;padding:5px 8px;z-index:10;max-width:calc(100% - 20px)}.thread-assembly-bar .orca-slider{width:100px}.thread-loupe-dock{display:none}.thread-status{white-space:pre-wrap;overflow-wrap:anywhere}.thread-stat{font:11px var(--font-mono);color:var(--text-main)}.thread-context-note{font-size:10.5px;color:var(--text-muted)}
body[data-mode="dock"] .thread-loupe{display:none}body[data-mode="dock"] .viewport-col>#gl-canvas,body[data-mode="dock"] .viewport-col>#vp-caliper-canvas{height:100%}body[data-mode="dock"] .viewport-col .vp-cut-bar{bottom:6px}body[data-mode="dock"] .thread-assembly-bar{bottom:40px;padding:3px 6px}body[data-mode="dock"] .thread-assembly-bar .vp-chip{padding:3px 6px;font-size:10px}body[data-mode="dock"] .thread-assembly-bar .ctrl-label{font-size:10px}body[data-mode="dock"][data-dock-tab="shape"] [data-thread-resource],body[data-mode="dock"][data-dock-tab="shape"] [data-thread-print],body[data-mode="dock"][data-dock-tab="presets"] [data-thread-shape],body[data-mode="dock"][data-dock-tab="presets"] [data-thread-resource],body[data-mode="dock"][data-dock-tab="textures"] [data-thread-print],body[data-mode="dock"][data-dock-tab="print"] [data-thread-resource]{display:none}body[data-mode="dock"][data-dock-tab="textures"] .thread-loupe-dock{display:flex}.thread-loupe-dock canvas{width:100%;height:120px}
</style></head><body data-mode="__INITIAL_MODE__" data-dock-tab="shape"><div class="studio-shell">  <header class="studio-header">
    <div class="brand-group">
      <div class="brand-logo" title="Orca Thread Studio">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M7 4h10v16H7z"/><path d="M5 8l14-4M5 12l14-4M5 16l14-4M5 20l14-4"/></svg>
      </div>
      <div class="brand-titles">
        <div class="brand-name-row">
          <span class="brand-title">Orca Thread Studio</span>
          <input id="inp-design-name" class="design-name-input" type="text" maxlength="80" value="Orca Thread" aria-label="Design Name" data-locale-aria="Design Name" />
        </div>
      </div>
      <button id="printer-pill" type="button" class="printer-pill" title="Clique para sincronizar impressora ativa do OrcaSlicer" data-locale-title="Sync active printer">
        <span class="printer-dot"></span>
        <span id="printer-pill-text" class="printer-pill-text">
          <span id="printer-pill-name" class="printer-pill-name">Generic 3D Printer</span>
          <span id="printer-pill-specs" class="printer-pill-specs">· 220×220×250 mm · 0.4mm</span>
        </span>
        <span id="printer-pill-sync" class="printer-pill-sync" aria-hidden="true">↻</span>
      </button>
    </div>

    <div class="header-actions">
      <button id="undo" class="btn btn-icon" title="Undo (Ctrl+Z)" data-locale-title="Undo" disabled>↶</button>
      <button id="redo" class="btn btn-icon" title="Redo (Ctrl+Y)" data-locale-title="Redo" disabled>↷</button>
      <button id="randomize" class="btn btn-soft">
        <span>🎲</span>
        <span data-i18n="btn_surprise">Surpreenda-me</span>
      </button>
      <button id="reset" class="btn btn-icon" title="Reset" data-locale-title="Reset">↺</button>
      <select id="language" class="btn" style="width:auto;padding:4px 5px" aria-label="Language" data-locale-aria="Language">__THREAD_LANGUAGE_OPTIONS__</select>
      <button id="theme" class="btn btn-icon" title="Dark / Light" data-locale-title="Theme">☾</button>
    </div>
  </header>

  <!-- DOCK MODE TABS -->
  <nav class="dock-tabs" aria-label="Studio Sections" data-locale-aria="Studio Sections">
    <button class="dock-tab-btn active" data-tab="shape" data-i18n="tab_shape">Forma</button>
    <button class="dock-tab-btn" data-tab="textures" data-i18n="tab_textures">Recursos</button>
    <button class="dock-tab-btn" data-tab="print" data-i18n="tab_print">Impressão</button>
    <button class="dock-tab-btn" data-tab="presets" data-i18n="tab_presets">Presets</button>
  </nav>

<main class="studio-workspace"><section class="col-panel col-left"><div class="col-scroll"><div id="card-presets" class="studio-card"><div class="card-head"><span class="card-title" data-i18n="sec_presets">Galeria de Modelos</span><button id="btn-toggle-save-preset" class="btn btn-soft" style="padding:2px 8px;font-size:10.5px;" data-i18n="btn_save_preset">+ Salvar</button></div><div id="save-preset-bar" class="save-preset-bar"><input id="inp-save-preset-name" class="save-preset-input" type="text" maxlength="64" placeholder="Nome do preset..."><button id="btn-confirm-save-preset" class="btn btn-accent" style="padding:4px 8px;" data-i18n="btn_ok">Salvar</button></div><div id="preset-filters" class="preset-filter-row"><button class="filter-chip active" data-cat="all" data-i18n="cat_all">Todos</button><button class="filter-chip" data-cat="container_and_lid" data-i18n="cat_container">Potes</button><button class="filter-chip" data-cat="standard_bottle_cap" data-i18n="cat_caps">Tampas</button><button class="filter-chip" data-cat="hose_vacuum_adapter" data-i18n="cat_adapters">Adaptadores</button><button class="filter-chip" data-cat="bolt_nut_knob" data-i18n="cat_bolts">Parafusos</button><button class="filter-chip" data-cat="user" data-i18n="cat_user">Meus</button></div><div id="presets-grid" class="presets-grid"></div></div><div id="card-silhouette" class="studio-card" data-thread-shape><div class="card-head"><span class="card-title" data-i18n="sec_shape">Forma & dimensões</span><span id="family-badge" class="card-badge">Pote</span></div><div id="fields-main"></div></div><div id="card-resolution" class="studio-card" data-thread-shape><div class="card-head"><span class="card-title" data-i18n="sec_thread">Rosca & resolução</span><span class="card-badge">mm</span></div><div id="fields-thread"></div></div><div id="card-measurements" class="studio-card" data-thread-shape hidden><div class="card-head"><span class="card-title" data-i18n="sec_measured">Mason 86 · medidas reais</span></div><p class="helper-note warn" data-i18n="mason_note">Meça o pote real. A geração exige confirmação manual.</p><div id="fields-measured"></div></div></div></section>    <section class="viewport-col">
      <canvas id="gl-canvas"></canvas>
      <canvas id="vp-caliper-canvas"></canvas>

      <!-- Top-Left Material & View Controls -->
      <div class="vp-toolbar-left">
        <select id="sel-material" class="vp-select" aria-label="Material" data-locale-aria="Material">
          <option value="emerald_silk" data-i18n="mat_emerald">Seda Esmeralda Orca</option>
          <option value="terracotta" data-i18n="mat_terracotta">Cerâmica Terracota</option>
          <option value="matte_ceramic" data-i18n="mat_white">Porcelana Branca Mate</option>
          <option value="copper_bronze" data-i18n="mat_copper">Bronze Cobre Escovado</option>
          <option value="xray" data-i18n="mat_xray">🔬 Raio-X / Parede (Translúcido)</option>
          <option value="heatmap" data-i18n="mat_heatmap">Mapa de Overhang (°)</option>
        </select>
        <button id="btn-vp-xray" class="vp-chip vp-chip-xray" data-i18n="vp_xray">🔬 Raio-X / Parede</button>
        <button id="btn-vp-calipers" class="vp-chip" data-i18n="vp_calipers">📏 Cotas mm</button>
        <button id="btn-vp-heatmap" class="vp-chip" data-i18n="vp_heatmap">🔥 Overhang</button>
        <button id="btn-vp-wire" class="vp-chip" data-i18n="vp_wire">⌗ Malha</button>
        <button id="btn-vp-spin" class="vp-chip" title="Auto-Rotate" data-locale-title="Auto-Rotate">⟳</button>
      </div>

      <!-- Out-of-bed live warning -->
      <div id="bed-alert-banner" class="bed-alert-banner">
        <span>⚠</span>
        <span id="bed-alert-text">Dimensões excedem o volume da impressora!</span>
      </div>

      <!-- Top-Right Live Printability & Dimensions HUD -->
      <aside id="vp-hud-right" class="vp-hud-right vp-glass">
        <div class="hud-title-row">
          <span data-i18n="hud_title">Inspeção geométrica</span>
          <span id="hud-status-pill" class="hud-status-pill ok">OK</span>
        </div>
        <div class="hud-grid">
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_wall_floor">Parede / Fundo</span>
            <span id="hud-wall-floor" class="hud-metric-v">2.4 / 3.2 mm</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_mouth_hole">Ø nominal</span>
            <span id="hud-mouth-hole" class="hud-metric-v">Ø 85.2 mm</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_dims">Dimensões (mm)</span>
            <span id="hud-dims" class="hud-metric-v">116×116×160</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_overhang">Overhang Máx</span>
            <span id="hud-overhang" class="hud-metric-v">28.4°</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_weight">Filamento Est.</span>
            <span id="hud-weight" class="hud-metric-v">~48 g</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_Tris">Triângulos</span>
            <span id="hud-tris" class="hud-metric-v">—</span>
          </div>
        </div>
        <div id="xray-legend" class="heatmap-legend">
          <span><i class="legend-swatch" style="background:#0fd6c2"></i><span data-i18n="leg_outer">Externa</span></span>
          <span><i class="legend-swatch" style="background:#ff8c38"></i><span data-i18n="leg_inner">Cavidade &amp; Fundo</span></span>
        </div>
        <div id="heatmap-legend" class="heatmap-legend">
          <span><i class="legend-swatch" style="background:#00c853"></i>≤45°</span>
          <span><i class="legend-swatch" style="background:#ffb300"></i>45–55°</span>
          <span><i class="legend-swatch" style="background:#ff3d00"></i>&gt;55°</span>
        </div>
        <div id="hud-warnings" class="hud-warnings"></div>
      </aside>

      <div class="thread-assembly-bar vp-glass"><button id="animate" class="vp-chip" data-i18n="animate">Rosquear</button><span class="ctrl-label" data-i18n="explode">Abertura</span><input id="explode" class="orca-slider" aria-label="Opening" data-locale-aria="Opening" type="range" min="0" max="40" step=".5" value="8"><span id="opening-mm" class="ctrl-unit">8 mm</span></div>
      <!-- Camera Preset Pills -->
      <div class="vp-cam-bar">
        <button class="vp-chip" data-cam="iso">Iso</button>
        <button class="vp-chip" data-cam="front" data-i18n="cam_front">Frente</button>
        <button class="vp-chip" data-cam="top" data-i18n="cam_top">Topo</button>
        <button class="vp-chip" data-cam="bottom" data-i18n="cam_bottom">Base</button>
        <button class="vp-chip" data-cam="fit" data-i18n="cam_fit">Enquadrar</button>
      </div>

      <!-- Bottom Dual Section Inspector Slider (Vertical Profile Y + Horizontal Plan Slice Z) -->
      <div class="vp-cut-bar vp-glass">
        <div class="vp-cut-modes" role="group" aria-label="Section Cut Mode" data-locale-aria="Section Cut Mode">
          <button id="cut" class="vp-cut-mode-btn active" data-i18n="vp_cut_y">✂ Corte Vertical (Perfil Y)</button>
          <button id="btn-cut-mode-z" class="vp-cut-mode-btn" data-i18n="vp_cut_z">💿 Fatia Horizontal Z (Planta 5%–100%)</button>
        </div>
        <input id="inp-cross-cut" class="orca-slider" type="range" min="0" max="100" step="1" value="0" />
        <span id="lbl-cross-cut" class="ctrl-num" style="width:62px;text-align:center;">Off</span>
        <button id="btn-cut-half" class="btn" style="padding:3px 7px;font-size:10.5px;">50%</button>
        <button id="btn-cut-off" class="btn" style="padding:3px 7px;font-size:10.5px;">Off</button>
      </div>
      <div class="thread-loupe"><div class="card-head"><span class="card-title" data-i18n="loupe">Lupa de flancos · seção axial</span><span id="engagement-readout" class="card-badge">—</span></div><canvas id="thread-loupe" aria-label="Thread engagement section" data-locale-aria="Thread engagement section"></canvas><div class="thread-loupe-legend"><span><i class="thread-key male"></i><span data-i18n="male">Macho</span></span><span><i class="thread-key female"></i><span data-i18n="female">Fêmea</span></span><span id="clearance-readout"></span></div></div>
    </section>

<section class="col-panel col-right"><div class="col-scroll"><div id="card-print-mode" class="studio-card" data-thread-print style="border-color:var(--orca-accent-border)"><div class="card-head"><span class="card-title" data-i18n="sec_fit">Encaixe & paredes</span><span id="fit-badge" class="card-badge">cᵣ 0.13 mm</span></div><div id="fields-fit"></div><div class="thread-dimension-grid"><div class="helper-note"><span data-i18n="lead">Avanço por volta</span><div id="lead" class="thread-stat">—</div></div><div class="helper-note"><span data-i18n="radial">Folga radial nominal</span><div id="radial" class="thread-stat">—</div></div></div><div id="warning" class="helper-note warn" hidden></div><p class="thread-context-note" data-i18n="physical">Imprima o calibrador antes da peça final.</p></div><div id="card-thread-options" class="studio-card" data-thread-resource><div class="card-head"><span class="card-title" data-i18n="sec_helix">Entradas & Higbee</span></div><div id="fields-helix"></div></div><div id="card-textures" class="studio-card" data-thread-resource><div class="card-head"><span class="card-title" data-i18n="sec_surface">Superfície</span></div><div id="fields-surface"></div></div><div id="card-envelope" class="studio-card" data-thread-resource><div class="card-head"><span class="card-title" data-i18n="sec_connections">Conexões</span></div><div id="fields-connections"></div></div><div id="card-gardening" class="studio-card" data-thread-print><div class="card-head"><span class="card-title" data-i18n="sec_gasket">Canal de vedação</span></div><div id="fields-gasket"></div></div><div id="card-print-settings" class="studio-card" data-thread-print><div class="card-head"><span class="card-title" data-i18n="sec_output">Impressão & exportação</span></div><label class="ctrl-row"><span class="ctrl-label" data-i18n="target">Peças</span><select id="target" class="vp-select thread-select"></select></label><div id="fields-print"></div><p class="helper-note" data-i18n="settings">5 paredes e camada fina para roscas.</p><div id="status" class="helper-note thread-status" role="status" aria-live="polite"></div></div><div class="studio-card thread-loupe-dock" data-thread-resource><div class="card-head"><span class="card-title" data-i18n="loupe">Lupa de flancos</span></div><canvas id="thread-loupe-dock" aria-label="Thread engagement section" data-locale-aria="Thread engagement section"></canvas><span id="dock-engagement" class="thread-context-note"></span></div></div>      <footer class="action-footer">
        <button class="btn-hero" id="send" data-action="send_to_plater">
          <span>🚀</span>
          <span data-i18n="btn_send_plater">Enviar para a Mesa do OrcaSlicer</span>
        </button>
        <div class="export-btn-row">
          <button class="btn" id="three" data-action="export_3mf">💾 <span data-i18n="btn_exp_3mf">Exportar .3MF</span></button>
          <button class="btn" id="stl" data-action="export_stl">📐 <span data-i18n="btn_exp_stl">Exportar .STL</span></button>
          <button class="btn btn-icon" id="folder" data-action="open_folder" title="Open Exports Folder" data-locale-title="Open export folder">📂</button>
        </div>
      </footer></section></main>  <footer class="action-footer dock-global-footer">
    <button class="btn-hero" data-action="send_to_plater" style="padding:8px 10px;font-size:12px;">
      <span>🚀</span>
      <span data-i18n="btn_send_plater">Enviar para a Mesa do OrcaSlicer</span>
    </button>
    <div class="export-btn-row">
      <button class="btn" data-action="export_3mf">💾 .3MF</button>
      <button class="btn" data-action="export_stl">📐 .STL</button>
      <button class="btn btn-icon" data-action="open_folder" title="Open Exports Folder" data-locale-title="Open export folder">📂</button>
    </div>
  </footer></div><div id="toast-banner" class="toast-banner" role="status" aria-live="polite"></div><script>
(function () {
  "use strict";
  const BOOT_PAYLOAD = __THREAD_BOOT_JSON__;
  let params = { ...BOOT_PAYLOAD.params },
    lang = BOOT_PAYLOAD.lang,
    theme = BOOT_PAYLOAD.theme,
    host = BOOT_PAYLOAD.host || {},
    meshes = [],
    profile = null,
    report = null,
    userPresets = BOOT_PAYLOAD.user_presets || [],
    builtins = BOOT_PAYLOAD.builtin_presets || [],
    presetFilter = "all",
    activePreset = "",
    updateTimer = null,
    currentWarning = "",
    lastStatus = null;
  let editRevision = 0,
    acknowledgedRevision = 0,
    languageRequest = 0,
    languageRevision = 0,
    userOverrodeTheme = false;
  const clientId = "thread-" + Math.random().toString(36).slice(2);
  const view = {
    yaw: -0.95,
    pitch: 0.48,
    zoom: 1,
    material: "emerald_silk",
    xray: false,
    wire: false,
    calipers: false,
    heatmap: false,
    cutAxis: "y",
    cutPct: 0,
    opening: 8,
    spin: 0,
    animate: false,
    autoSpin: false,
  };
  const words = {
    pt: {
      reset: "Resetar",
      subtitle: "Roscas, potes e adaptadores · projeto paramétrico",
      parameters: "Parâmetros",
      preview: "Visualização",
      output: "Exportação",
      presets: "Biblioteca de projetos",
      save: "Salvar preset",
      remove: "Excluir",
      fit: "Enquadrar",
      cut: "Corte axial",
      animate: "Rosquear",
      explode: "Abertura",
      loupe: "Lupa de flancos · seção axial",
      male: "Macho",
      female: "Fêmea",
      analysis: "Análise de encaixe",
      radial: "Folga radial nominal",
      lead: "Avanço por volta",
      physical:
        "O encaixe depende do filamento e da impressora. Imprima o calibrador antes da peça final.",
      target: "Peças",
      send: "Enviar para a mesa",
      folder: "Abrir pasta de exportações",
      printer: "Impressora conectada",
      settings:
        "3MF: 5 paredes, 5 camadas de topo/base e camada fina para as roscas. As peças são distribuídas sem alterar a escala.",
      experimental:
        "Experimental: perfil simplificado; encaixe físico não homologado. Sem garantia de vedação, pressão ou uso alimentar.",
      clear: "Sem interferência no envelope analítico",
      waiting: "Aguardando o host do OrcaSlicer.",
      local:
        "A prévia depende do plugin nativo. Abra este estúdio no OrcaSlicer.",
      notch: "Anéis: 1 / 2 / 3 entalhes = 0,10 / 0,18 / 0,26 mm",
    },
    en: {
      reset: "Reset",
      subtitle: "Threads, containers and adapters · parametric design",
      parameters: "Parameters",
      preview: "Preview",
      output: "Export",
      presets: "Project library",
      save: "Save preset",
      remove: "Delete",
      fit: "Fit view",
      cut: "Axial section",
      animate: "Screw motion",
      explode: "Opening",
      loupe: "Thread loupe · axial section",
      male: "Male",
      female: "Female",
      analysis: "Engagement analysis",
      radial: "Nominal radial clearance",
      lead: "Lead per revolution",
      physical:
        "Fit depends on your filament and printer. Print calibration rings before the final part.",
      target: "Parts",
      send: "Send to plater",
      folder: "Open export folder",
      printer: "Connected printer",
      settings:
        "3MF: 5 walls, 5 top/bottom layers and fine thread layers. Parts are arranged at their original scale.",
      experimental:
        "Experimental: simplified profile; physical fit is unverified. No sealing, pressure or food-use guarantee.",
      clear: "No analytical envelope interference",
      waiting: "Waiting for the OrcaSlicer host.",
      local:
        "Preview requires the native plugin. Open this studio in OrcaSlicer.",
      notch: "Rings: 1 / 2 / 3 notches = 0.10 / 0.18 / 0.26 mm",
    },
  };
  const labels = {
    module: ["Tipo de projeto", "Project type"],
    standard: ["Perfil de rosca", "Thread profile"],
    part: ["Peça de garrafa", "Bottle part"],
    name: ["Nome", "Name"],
    nominal_dia: ["Diâmetro nominal · mm", "Nominal diameter · mm"],
    pitch: ["Passo axial · mm", "Axial pitch · mm"],
    thread_length: ["Comprimento roscado · mm", "Thread length · mm"],
    starts: ["Entradas", "Starts"],
    hand: ["Sentido", "Handedness"],
    diameter: ["Diâmetro do corpo · mm", "Body diameter · mm"],
    height: ["Altura do pote · mm", "Container height · mm"],
    wall_thickness: ["Parede · mm", "Wall · mm"],
    floor_thickness: ["Fundo · mm", "Floor · mm"],
    diametral_clearance: ["Folga diametral · mm", "Diametral clearance · mm"],
    axial_clearance: ["Folga axial · mm", "Axial clearance · mm"],
    higbee_turns: ["Higbee · voltas", "Higbee · turns"],
    texture: ["Textura", "Texture"],
    knurl_depth: ["Profundidade da textura · mm", "Texture depth · mm"],
    knurl_count: ["Repetições da textura", "Texture repeats"],
    head: ["Cabeça / porca", "Head / nut"],
    head_height: ["Altura da cabeça · mm", "Head height · mm"],
    bore_diameter: ["Furo do parafuso · mm", "Bolt bore · mm"],
    inlet_diameter: ["Entrada · mm", "Inlet · mm"],
    outlet_diameter: ["Saída · mm", "Outlet · mm"],
    adapter_length: ["Comprimento total · mm", "Overall length · mm"],
    end_length: ["Comprimento das pontas · mm", "End length · mm"],
    end_a: ["Ponta de entrada", "Inlet end"],
    end_b: ["Ponta de saída", "Outlet end"],
    gasket: ["Canal para vedação", "Gasket groove"],
    gasket_width: ["Largura do canal · mm", "Groove width · mm"],
    gasket_depth: ["Profundidade do canal · mm", "Groove depth · mm"],
    gasket_offset: ["Recuo do canal · mm", "Groove inset · mm"],
    auto_configure_slicer: ["Ajustar fatiamento", "Configure slicing"],
    measurements_confirmed: [
      "Confirmo as medidas reais",
      "I confirm measured dimensions",
    ],
    measured_major_dia: [
      "Mason 86: diâmetro maior",
      "Mason 86: major diameter",
    ],
    measured_root_dia: [
      "Mason 86: diâmetro da raiz",
      "Mason 86: root diameter",
    ],
    measured_pitch: ["Mason 86: passo medido", "Mason 86: measured pitch"],
    measured_length: ["Mason 86: comprimento", "Mason 86: thread length"],
  };
  const options = {
    module: [
      ["container_and_lid", "Pote + tampa", "Container + lid"],
      ["standard_bottle_cap", "Tampa / gargalo", "Bottle cap / neck"],
      ["hose_vacuum_adapter", "Adaptador", "Hose adapter"],
      ["bolt_nut_knob", "Parafuso + porca", "Bolt + nut"],
    ],
    standard: [
      ["fdm_trapezoid_45", "FDM 45°", "FDM 45°"],
      ["iso_metric", "Métrica 60°", "Metric 60°"],
      ["pco1881", "PCO-1881 experimental", "PCO-1881 experimental"],
      ["mason_70", "Mason 70 experimental", "Mason 70 experimental"],
      ["mason_86", "Mason 86 · medir", "Mason 86 · measure"],
    ],
    part: [
      ["cap", "Tampa", "Cap"],
      ["neck", "Gargalo", "Neck"],
    ],
    starts: [
      ["1", "1", "1"],
      ["2", "2", "2"],
      ["3", "3", "3"],
    ],
    hand: [
      ["right", "Direita", "Right"],
      ["left", "Esquerda", "Left"],
    ],
    texture: [
      ["knurled", "Recartilhado", "Knurled"],
      ["fluted", "Canelado", "Fluted"],
      ["smooth", "Liso", "Smooth"],
      ["faceted", "Facetado", "Faceted"],
    ],
    head: [
      ["hex", "Sextavada", "Hex"],
      ["knurled", "Recartilhada", "Knurled"],
      ["wing", "Borboleta", "Wing"],
    ],
    end_a: [
      ["smooth", "Liso cônico", "Smooth tapered"],
      ["barb", "Espigão", "Barb"],
      ["male", "Rosca macho", "Male thread"],
      ["female", "Rosca fêmea", "Female thread"],
    ],
    export_target: [
      ["all", "Conjunto", "All parts"],
      ["primary", "Peça principal", "Primary part"],
      ["secondary", "Peça secundária", "Secondary part"],
      ["calibration", "3 anéis de calibração", "3 calibration rings"],
    ],
  };
  options.end_b = options.end_a;
  const ranges = {
    nominal_dia: [6, 100, 0.1],
    pitch: [0.5, 10, 0.05],
    thread_length: [3, 100, 0.1],
    starts: [1, 3, 1],
    diameter: [12, 150, 0.1],
    height: [12, 200, 0.1],
    wall_thickness: [1.2, 8, 0.1],
    floor_thickness: [1.2, 8, 0.1],
    diametral_clearance: [0.05, 0.6, 0.01],
    axial_clearance: [0, 0.6, 0.01],
    higbee_turns: [0.1, 1, 0.05],
    knurl_depth: [0, 1.5, 0.1],
    knurl_count: [12, 100, 1],
    head_height: [3, 15, 0.1],
    bore_diameter: [0, 90, 0.1],
    inlet_diameter: [10, 100, 0.1],
    outlet_diameter: [10, 120, 0.1],
    adapter_length: [30, 180, 0.1],
    end_length: [7, 35, 0.1],
  };

  Object.assign(words.pt, {
    btn_surprise: "Surpreenda-me",
    tab_shape: "Forma",
    tab_textures: "Recursos",
    tab_print: "Impressão",
    tab_presets: "Presets",
    sec_presets: "Galeria de Modelos",
    btn_save_preset: "+ Salvar",
    btn_ok: "Salvar",
    cat_all: "Todos",
    cat_container: "Potes",
    cat_caps: "Tampas",
    cat_adapters: "Adaptadores",
    cat_bolts: "Parafusos",
    cat_user: "Meus",
    sec_shape: "Forma & dimensões",
    sec_thread: "Rosca & resolução",
    sec_measured: "Mason 86 · medidas reais",
    mason_note:
      "Meça o pote real. A geração exige confirmação manual; o perfil permanece experimental.",
    sec_fit: "Encaixe & paredes",
    sec_helix: "Entradas & Higbee",
    sec_surface: "Superfície",
    sec_connections: "Conexões",
    sec_gasket: "Canal de vedação",
    sec_output: "Impressão & exportação",
    btn_send_plater: "Enviar para a Mesa do OrcaSlicer",
    btn_exp_3mf: "Exportar .3MF",
    btn_exp_stl: "Exportar .STL",
    mat_emerald: "Seda Esmeralda Orca",
    mat_terracotta: "Cerâmica Terracota",
    mat_white: "Porcelana Branca Mate",
    mat_copper: "Bronze Cobre Escovado",
    mat_xray: "🔬 Raio-X / Parede (Translúcido)",
    mat_heatmap: "Mapa de Overhang (°)",
    vp_xray: "🔬 Raio-X / Parede",
    vp_calipers: "📏 Cotas mm",
    vp_heatmap: "🔥 Overhang",
    vp_wire: "⌗ Malha",
    hud_title: "Inspeção geométrica",
    hud_wall_floor: "Parede / Fundo",
    hud_mouth_hole: "Ø nominal",
    hud_dims: "Dimensões da prévia (mm)",
    hud_overhang: "Overhang geométrico",
    hud_weight: "Filamento Est.",
    hud_Tris: "Triângulos",
    leg_outer: "Externa",
    leg_inner: "Cavidade & Fundo",
    cam_front: "Frente",
    cam_top: "Topo",
    cam_bottom: "Base",
    cam_fit: "Enquadrar",
    vp_cut_y: "✂ Corte Vertical (Perfil Y)",
    vp_cut_z: "💿 Fatia Horizontal Z",
    fitPrinter: "Prévia excede o volume da impressora",
    resolution: "Resolução angular",
    noEngagement: "Tampa fora da região de engate",
    interference: "Interferência nesta posição",
  });
  Object.assign(words.en, {
    btn_surprise: "Surprise me",
    tab_shape: "Shape",
    tab_textures: "Features",
    tab_print: "Print",
    tab_presets: "Presets",
    sec_presets: "Model Gallery",
    btn_save_preset: "+ Save",
    btn_ok: "Save",
    cat_all: "All",
    cat_container: "Jars",
    cat_caps: "Caps",
    cat_adapters: "Adapters",
    cat_bolts: "Bolts",
    cat_user: "Mine",
    sec_shape: "Shape & dimensions",
    sec_thread: "Thread & resolution",
    sec_measured: "Mason 86 · real measurements",
    mason_note:
      "Measure the real jar. Generation requires manual confirmation; the profile remains experimental.",
    sec_fit: "Fit & walls",
    sec_helix: "Starts & Higbee",
    sec_surface: "Surface",
    sec_connections: "Connections",
    sec_gasket: "Gasket channel",
    sec_output: "Print & export",
    btn_send_plater: "Send to OrcaSlicer Plater",
    btn_exp_3mf: "Export .3MF",
    btn_exp_stl: "Export .STL",
    mat_emerald: "Orca Emerald Silk",
    mat_terracotta: "Terracotta Clay",
    mat_white: "Matte White Porcelain",
    mat_copper: "Brushed Copper Bronze",
    mat_xray: "🔬 X-Ray / Wall (Translucent)",
    mat_heatmap: "Overhang Map (°)",
    vp_xray: "🔬 X-Ray / Wall",
    vp_calipers: "📏 Dimensions mm",
    vp_heatmap: "🔥 Overhang",
    vp_wire: "⌗ Wireframe",
    hud_title: "Geometry inspection",
    hud_wall_floor: "Wall / Floor",
    hud_mouth_hole: "Nominal Ø",
    hud_dims: "Preview dimensions (mm)",
    hud_overhang: "Geometric overhang",
    hud_weight: "Est. Filament",
    hud_Tris: "Triangles",
    leg_outer: "Outer",
    leg_inner: "Cavity & Floor",
    cam_front: "Front",
    cam_top: "Top",
    cam_bottom: "Bottom",
    cam_fit: "Fit view",
    vp_cut_y: "✂ Vertical section (Y)",
    vp_cut_z: "💿 Horizontal Z slice",
    fitPrinter: "Preview exceeds the printer envelope",
    resolution: "Angular resolution",
    noEngagement: "Lid outside engagement region",
    interference: "Interference at this position",
  });
  labels.resolution = ["Resolução angular", "Angular resolution"];
  ranges.resolution = [48, 192, 12];
  Object.assign(ranges, {
    gasket_width: [0.6, 2, 0.1],
    gasket_depth: [0.2, 1.2, 0.1],
    gasket_offset: [0.6, 3, 0.1],
    measured_major_dia: [0, 120, 0.1],
    measured_root_dia: [0, 120, 0.1],
    measured_pitch: [0, 10, 0.05],
    measured_length: [0, 40, 0.1],
  });
  function normalizeLanguage(value) {
    let code = String(value || "en").trim().toLowerCase().replaceAll("_", "-").split(/[.@]/)[0];
    while (code) {
      if (BOOT_PAYLOAD.languages.some(item => item.code === code)) return code;
      code = code.includes("-") ? code.slice(0, code.lastIndexOf("-")) : "";
    }
    return "en";
  }
  function localeText(english, portuguese = english) {
    return BOOT_PAYLOAD.translations[lang]?.[english] || (lang === "pt" ? portuguese : english);
  }
  function text(key) {
    return localeText(words.en[key] || key, words.pt[key] || words.en[key] || key);
  }
  const clone = (value) => JSON.parse(JSON.stringify(value));
  function radialProfile(q, female, candidate) {
    const p = candidate || params,
      phase = q / p.pitch,
      signed = ((((phase + 0.5) % 1) + 1) % 1) - 0.5;
    let depth =
      p.standard === "pco1881"
        ? 1.6
        : p.standard === "mason_86" && p.measurements_confirmed
          ? (p.measured_major_dia - p.measured_root_dia) / 2
          : Math.min(
              p.nominal_dia * 0.12,
              p.pitch * (p.standard === "iso_metric" ? 0.61343 : 0.375),
            );
    const widen = female ? p.axial_clearance / p.pitch / 2 : 0;
    function tooth(v) {
      const q = ((((v + 0.5) % 1) + 1) % 1) - 0.5;
      if (p.standard === "pco1881")
        return q < -0.12
          ? Math.max(0, Math.min(1, (q + 0.31) / 0.19))
          : q > 0.1
            ? Math.max(0, Math.min(1, (0.3 - q) / 0.2))
            : 1;
      const crest = p.standard === "iso_metric" ? 0.0625 : 0.125,
        root =
          p.standard === "iso_metric" ? 0.0625 + 0.61343 / Math.sqrt(3) : 0.5;
      return Math.max(
        0,
        Math.min(1, (root - Math.max(0, Math.abs(q) - widen)) / (root - crest)),
      );
    }
    let f = tooth(phase);
    if (female && p.standard === "pco1881")
      for (let j = 0; j < 9; j++)
        f = Math.max(f, tooth(phase - widen + (2 * widen * j) / 8));
    const u = Math.max(
        0,
        Math.min(
          1,
          Math.min(q, p.thread_length - q) / (p.lead * p.higbee_turns),
        ),
      ),
      envelope = u * u * (3 - 2 * u);
    return (
      p.nominal_dia / 2 -
      depth +
      depth * f * (female ? 1 : envelope) +
      (female ? p.diametral_clearance / 2 : 0)
    );
  }

  function mat4Identity() {
    const m = new Float32Array(16);
    m[0] = 1;
    m[5] = 1;
    m[10] = 1;
    m[15] = 1;
    return m;
  }

  function mat4Multiply(a, b) {
    const out = new Float32Array(16);
    for (let col = 0; col < 4; col++) {
      const b0 = b[col * 4],
        b1 = b[col * 4 + 1],
        b2 = b[col * 4 + 2],
        b3 = b[col * 4 + 3];
      out[col * 4] = a[0] * b0 + a[4] * b1 + a[8] * b2 + a[12] * b3;
      out[col * 4 + 1] = a[1] * b0 + a[5] * b1 + a[9] * b2 + a[13] * b3;
      out[col * 4 + 2] = a[2] * b0 + a[6] * b1 + a[10] * b2 + a[14] * b3;
      out[col * 4 + 3] = a[3] * b0 + a[7] * b1 + a[11] * b2 + a[15] * b3;
    }
    return out;
  }

  function mat4Perspective(fovyRad, aspect, near, far) {
    const f = 1.0 / Math.tan(0.5 * fovyRad);
    const nf = 1.0 / (near - far);
    const out = new Float32Array(16);
    out[0] = f / Math.max(aspect, 0.05);
    out[5] = f;
    out[10] = (far + near) * nf;
    out[11] = -1.0;
    out[14] = 2.0 * far * near * nf;
    return out;
  }

  function mat4LookAtZUp(eye, center) {
    let fx = center[0] - eye[0];
    let fy = center[1] - eye[1];
    let fz = center[2] - eye[2];
    const fl = Math.hypot(fx, fy, fz) || 1.0;
    fx /= fl;
    fy /= fl;
    fz /= fl;

    let upX = 0.0,
      upY = 0.0,
      upZ = 1.0;
    if (Math.abs(fz) > 0.999) {
      upY = 1.0;
      upZ = 0.0;
    }

    let sx = fy * upZ - fz * upY;
    let sy = fz * upX - fx * upZ;
    let sz = fx * upY - fy * upX;
    const sl = Math.hypot(sx, sy, sz) || 1.0;
    sx /= sl;
    sy /= sl;
    sz /= sl;

    const ux = sy * fz - sz * fy;
    const uy = sz * fx - sx * fz;
    const uz = sx * fy - sy * fx;

    const out = mat4Identity();
    out[0] = sx;
    out[4] = sy;
    out[8] = sz;
    out[12] = -(sx * eye[0] + sy * eye[1] + sz * eye[2]);
    out[1] = ux;
    out[5] = uy;
    out[9] = uz;
    out[13] = -(ux * eye[0] + uy * eye[1] + uz * eye[2]);
    out[2] = -fx;
    out[6] = -fy;
    out[10] = -fz;
    out[14] = fx * eye[0] + fy * eye[1] + fz * eye[2];
    out[3] = 0;
    out[7] = 0;
    out[11] = 0;
    out[15] = 1;
    return out;
  }

  function modelMatrix(index, parts = meshes, p = params, v = view) {
    const m = mat4Identity(),
      pair =
        parts.length === 2 &&
        p.export_target === "all" &&
        ["container_and_lid", "bolt_nut_knob"].includes(p.module);
    if (pair && index === 1) {
      const angle = v.spin * (p.hand === "left" ? -1 : 1),
        cs = Math.cos(angle),
        sn = Math.sin(angle);
      m[0] = cs;
      m[1] = sn;
      m[4] = sn;
      m[5] = -cs;
      m[10] = -1;
      m[14] =
        (p.module === "container_and_lid"
          ? p.height + p.floor_thickness
          : p.head_height + p.thread_length) +
        v.opening +
        (v.spin * p.lead) / (2 * Math.PI);
    } else if (parts.length > 1 && !pair) {
      const diameter = Math.max(
        ...parts.map((item) =>
          Math.max(
            ...(item.bounds?.size || [p.nominal_dia, p.nominal_dia]).slice(
              0,
              2,
            ),
          ),
        ),
      );
      m[12] = (index - (parts.length - 1) / 2) * diameter * 1.15;
    }
    return m;
  }
  function transformPoint(point, m) {
    return [
      m[0] * point[0] + m[4] * point[1] + m[8] * point[2] + m[12],
      m[1] * point[0] + m[5] * point[1] + m[9] * point[2] + m[13],
      m[2] * point[0] + m[6] * point[1] + m[10] * point[2] + m[14],
    ];
  }
  function getSceneBounds(parts = meshes, p = params, v = view) {
    const minimum = [Infinity, Infinity, Infinity],
      maximum = [-Infinity, -Infinity, -Infinity];
    parts.forEach((part, index) => {
      let bounds = part.bounds || part.bounds_mm;
      if (!bounds && part.vertices) {
        const a = part.vertices,
          lo = [Infinity, Infinity, Infinity],
          hi = [-Infinity, -Infinity, -Infinity];
        for (let j = 0; j < a.length; j += 3)
          for (let k = 0; k < 3; k++) {
            lo[k] = Math.min(lo[k], a[j + k]);
            hi[k] = Math.max(hi[k], a[j + k]);
          }
        bounds = { min: lo, max: hi };
      }
      if (!bounds) return;
      const m = modelMatrix(index, parts, p, v);
      for (let mask = 0; mask < 8; mask++) {
        const point = transformPoint(
          [0, 1, 2].map((k) =>
            mask & (1 << k) ? bounds.max[k] : bounds.min[k],
          ),
          m,
        );
        for (let k = 0; k < 3; k++) {
          minimum[k] = Math.min(minimum[k], point[k]);
          maximum[k] = Math.max(maximum[k], point[k]);
        }
      }
    });
    if (!parts.length || !minimum.every(Number.isFinite))
      return {
        min: [-20, -20, 0],
        max: [20, 20, 40],
        size: [40, 40, 40],
        center: [0, 0, 20],
        empty: true,
      };
    return {
      min: minimum,
      max: maximum,
      size: maximum.map((x, k) => x - minimum[k]),
      center: maximum.map((x, k) => (x + minimum[k]) / 2),
      empty: false,
    };
  }
  function fitCamera() {
    view.zoom = 1;
    view.yaw = -0.95;
    view.pitch = 0.48;
    return getSceneBounds();
  }
  function geometryRevisionIsStale(
    message,
    token = clientId,
    revision = editRevision,
    acknowledged = acknowledgedRevision,
  ) {
    if (
      message.client_id === token &&
      Number.isFinite(message.request_id) &&
      message.request_id < revision
    )
      return true;
    const acknowledgedRequest = message.client_acknowledgements?.[token];
    if (Number.isFinite(acknowledgedRequest) && acknowledgedRequest >= revision)
      return false;
    if (message.client_id === token && Number.isFinite(message.request_id))
      return message.request_id < revision;
    return revision > acknowledged;
  }
  function buildMutationPayload(
    payload,
    current,
    revision,
    acknowledged,
    token,
  ) {
    const message = { ...payload, request_id: revision + 1, client_id: token };
    if (revision > acknowledged) message.pending_params = clone(current);
    return message;
  }
  function resolveInitialState(
    message,
    current,
    token = clientId,
    revision = editRevision,
    acknowledged = acknowledgedRevision,
  ) {
    const acceptDesign = !geometryRevisionIsStale(
      message,
      token,
      revision,
      acknowledged,
    );
    return {
      acceptDesign,
      params: acceptDesign ? { ...message.params } : current.params,
      lang: acceptDesign ? message.lang || message.params.lang : current.lang,
      theme: acceptDesign
        ? resolveStudioTheme(
            message.theme || message.params.theme,
            message.host || current.host,
            current.theme,
            current.userOverrodeTheme,
          )
        : current.theme,
      host: message.host || current.host,
      userPresets: message.user_presets || current.userPresets,
      builtins: message.builtin_presets || current.builtins,
    };
  }
  function detectInjectedOrcaTheme() {
    if (
      typeof window === "undefined" ||
      typeof window.getComputedStyle !== "function"
    )
      return null;
    if (typeof document === "undefined" || !document.documentElement)
      return null;
    try {
      const style = window.getComputedStyle(document.documentElement);
      if (!style || typeof style.getPropertyValue !== "function") return null;
      const raw = String(style.getPropertyValue("--orca-bg") || "").trim();
      if (!raw) return null;
      let r = NaN,
        g = NaN,
        b = NaN;
      if (raw[0] === "#") {
        const hex = raw.slice(1).trim();
        if (hex.length === 3) {
          r = parseInt(hex[0] + hex[0], 16);
          g = parseInt(hex[1] + hex[1], 16);
          b = parseInt(hex[2] + hex[2], 16);
        } else if (hex.length >= 6) {
          r = parseInt(hex.slice(0, 2), 16);
          g = parseInt(hex.slice(2, 4), 16);
          b = parseInt(hex.slice(4, 6), 16);
        }
      } else {
        const m = raw.match(
          /rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)/i,
        );
        if (m) {
          r = parseFloat(m[1]);
          g = parseFloat(m[2]);
          b = parseFloat(m[3]);
        }
      }
      if (!Number.isFinite(r) || !Number.isFinite(g) || !Number.isFinite(b))
        return null;
      const lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0;
      return lum > 0.52 ? "light" : "dark";
    } catch (_) {
      return null;
    }
  }
  function resolveStudioTheme(
    candidate,
    hostState,
    currentTheme,
    overridden,
    injectedTheme = detectInjectedOrcaTheme(),
  ) {
    if (overridden) return currentTheme;
    if (
      hostState?.theme_explicit === false &&
      (injectedTheme === "light" || injectedTheme === "dark")
    )
      return injectedTheme;
    return candidate === "light" || candidate === "dark"
      ? candidate
      : currentTheme;
  }
  const hasDOM = typeof document !== "undefined";
  const globalObject = typeof window !== "undefined" ? window : globalThis;
  globalObject.__threadStudio = {
    getState: () => ({
      params: clone(params),
      lang,
      theme,
      host: clone(host),
      view: { ...view },
      meshCount: meshes.length,
    }),
    getSceneBounds,
    modelMatrix,
    transformPoint,
    fitCamera,
    radialProfile,
    geometryRevisionIsStale,
    buildMutationPayload,
    resolveInitialState,
    detectInjectedOrcaTheme,
    resolveStudioTheme,
  };
  if (!hasDOM) return;
  const $ = (id) => document.getElementById(id);
  let gl = null,
    meshProgram = null,
    lineProgram = null,
    gridBuffer = null,
    gridCount = 0,
    lastFrame = 0,
    lastCamera = null,
    drag = null,
    toastTimer;
  function send(payload) {
    try {
      if (window.orca && typeof window.orca.postMessage === "function") {
        window.orca.postMessage(payload);
        return true;
      }
      if (window.chrome?.webview) {
        window.chrome.webview.postMessage(payload);
        return true;
      }
    } catch (error) {
      status(String(error), true);
    }
    return false;
  }
  function status(message, error = false, paths = []) {
    lastStatus = {source: message, error, paths};
    const localized = localeText(message) + (paths.length ? "\n" + paths.join("\n") : "");
    $("status").textContent = localized;
    $("status").classList.toggle("warn", error);
    const toast = $("toast-banner");
    toast.textContent = localized;
    toast.classList.toggle("error", error);
    toast.classList.add("visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(
      () => toast.classList.remove("visible"),
      error ? 7000 : 3200,
    );
  }
  function sendMutation(payload) {
    clearTimeout(updateTimer);
    updateTimer = null;
    const message = buildMutationPayload(
      payload,
      params,
      editRevision,
      acknowledgedRevision,
      clientId,
    );
    editRevision = message.request_id;
    return send(message);
  }
  function scheduleUpdate() {
    clearTimeout(updateTimer);
    editRevision += 1;
    const revision = editRevision;
    updateTimer = setTimeout(() => {
      if (
        !send({
          type: "update",
          params,
          request_id: revision,
          client_id: clientId,
        })
      )
        status(words.en.local, true);
    }, 180);
  }
  function change(key, value) {
    params[key] = value;
    syncControls();
    scheduleUpdate();
  }
  function optionFill(element, rows, value) {
    element.replaceChildren();
    rows.forEach((row) => {
      const option = document.createElement("option");
      option.value = row[0];
      option.textContent = localeText(row[2], row[1]);
      element.append(option);
    });
    element.value = String(value);
  }

  function control(key) {
    const wrapper = document.createElement("div");
    wrapper.dataset.field = key;
    const source = labels[key] || [key, key];
    const label = localeText(source[1], source[0]);
    const visibleLabel = localeText(source[1].replace(/\s*·\s*(mm|turns)\s*$/u, ""), source[0].replace(/\s*·\s*(mm|voltas)\s*$/u, ""));
    if (typeof params[key] === "boolean") {
      wrapper.className = "switch-row";
      const title = document.createElement("span");
      title.className = "ctrl-label";
      title.textContent = visibleLabel;
      const toggle = document.createElement("label");
      toggle.className = "toggle-switch";
      const input = document.createElement("input");
      input.type = "checkbox";
      input.dataset.key = key;
      input.id = "chk-" + key;
      input.checked = params[key];
      input.setAttribute("aria-label", label);
      input.onchange = () => change(key, input.checked);
      const track = document.createElement("span");
      track.className = "toggle-track";
      toggle.append(input, track);
      wrapper.append(title, toggle);
      return wrapper;
    }
    wrapper.className = "ctrl-row";
    const top = document.createElement("div");
    top.className = "ctrl-top";
    const title = document.createElement("span");
    title.className = "ctrl-label";
    title.textContent = visibleLabel;
    top.append(title);
    wrapper.append(top);
    if (options[key]) {
      const select = document.createElement("select");
      select.className = "vp-select thread-select";
      select.dataset.key = key;
      select.id = "sel-" + key;
      select.setAttribute("aria-label", label);
      optionFill(select, options[key], params[key]);
      select.onchange = () =>
        change(key, key === "starts" ? Number(select.value) : select.value);
      wrapper.append(select);
      return wrapper;
    }
    wrapper.dataset.slider = key;
    const valueWrap = document.createElement("div");
    valueWrap.className = "ctrl-val-wrap";
    const number = document.createElement("input");
    number.type = "number";
    number.className = "ctrl-num";
    number.dataset.key = key;
    number.id = "num-" + key;
    number.setAttribute("aria-label", label);
    const unit = document.createElement("span");
    unit.className = "ctrl-unit";
    unit.textContent = ["starts", "knurl_count", "resolution"].includes(key)
      ? ""
      : key === "higbee_turns"
        ? "↻"
        : "mm";
    const range = document.createElement("input");
    range.type = "range";
    range.className = "orca-slider";
    range.dataset.range = key;
    range.id = "range-" + key;
    range.setAttribute("aria-label", label);
    const limits = ranges[key] || [0, 200, 0.1];
    [number, range].forEach((input) => {
      [input.min, input.max, input.step] = limits;
      input.value = params[key];
    });
    number.onchange = () => change(key, Number(number.value));
    range.oninput = () => change(key, Number(range.value));
    valueWrap.append(number, unit);
    top.append(valueWrap);
    wrapper.append(range);
    return wrapper;
  }
  const groups = {
    main: [
      "module",
      "part",
      "diameter",
      "height",
      "inlet_diameter",
      "outlet_diameter",
      "adapter_length",
      "head",
      "head_height",
      "bore_diameter",
    ],
    thread: ["standard", "nominal_dia", "pitch", "thread_length", "resolution"],
    fit: [
      "wall_thickness",
      "floor_thickness",
      "diametral_clearance",
      "axial_clearance",
    ],
    helix: ["starts", "hand", "higbee_turns"],
    surface: ["texture", "knurl_depth", "knurl_count"],
    connections: ["end_a", "end_b", "end_length"],
    gasket: ["gasket", "gasket_width", "gasket_depth", "gasket_offset"],
    print: ["auto_configure_slicer"],
    measured: [
      "measured_major_dia",
      "measured_root_dia",
      "measured_pitch",
      "measured_length",
      "measurements_confirmed",
    ],
  };
  function buildControls() {
    for (const [group, keys] of Object.entries(groups)) {
      const box = $("fields-" + group);
      box.replaceChildren(...keys.map(control));
    }
    optionFill($("target"), options.export_target, params.export_target);
    syncControls();
  }
  function syncControls() {
    document.querySelectorAll("[data-key]").forEach((element) => {
      if (element.type === "checkbox")
        element.checked = params[element.dataset.key];
      else element.value = params[element.dataset.key];
    });
    document
      .querySelectorAll("[data-range]")
      .forEach((element) => (element.value = params[element.dataset.range]));
    $("target").value = params.export_target;
    $("inp-design-name").value = params.name;
    const family = params.module,
      bottle = family === "standard_bottle_cap",
      adapter = family === "hose_vacuum_adapter",
      bolt = family === "bolt_nut_knob";
    document.querySelectorAll("[data-field]").forEach((element) => {
      const key = element.dataset.field;
      let visible = true;
      if (key === "part") visible = bottle;
      if (["diameter", "height"].includes(key))
        visible = family === "container_and_lid";
      if (["head", "head_height", "bore_diameter"].includes(key))
        visible = bolt;
      if (
        [
          "inlet_diameter",
          "outlet_diameter",
          "adapter_length",
          "end_a",
          "end_b",
          "end_length",
        ].includes(key)
      )
        visible = adapter;
      if (key === "floor_thickness") visible = !adapter;
      if (["knurl_count", "knurl_depth"].includes(key))
        visible = params.texture !== "smooth";
      element.hidden = !visible;
      const locked =
        bottle &&
        ["pco1881", "mason_70"].includes(params.standard) &&
        ["nominal_dia", "pitch", "thread_length", "starts"].includes(key);
      element
        .querySelectorAll("input,select")
        .forEach((input) => (input.disabled = locked));
    });
    $("card-envelope").hidden = !adapter;
    $("card-gardening").hidden = adapter || bolt;
    $("card-measurements").hidden = !(bottle && params.standard === "mason_86");
    const selectedFamily = options.module.find(row => row[0] === family);
    $("family-badge").textContent = selectedFamily ? localeText(selectedFamily[2], selectedFamily[1]) : family;
  }
  function miniSvg(p) {
    const family = p.module;
    let shape;
    if (family === "hose_vacuum_adapter")
      shape = '<path d="M8 4h14v8l-4 13v7h-6v-7L8 12Z"/>';
    else if (family === "bolt_nut_knob")
      shape =
        '<path d="M5 3h20v6H5Zm6 6h8v23h-8Z"/><path d="m10 15 10-3m-10 8 10-3m-10 8 10-3m-10 8 10-3"/>';
    else if (family === "standard_bottle_cap")
      shape =
        '<path d="M5 9Q15 3 25 9v19Q15 34 5 28Z"/><path d="M5 14q10 6 20 0m-20 6q10 6 20 0"/>';
    else
      shape =
        '<path d="M6 9Q15 5 24 9v21Q15 35 6 30ZM5 4Q15 0 25 4v5Q15 13 5 9Z"/><path d="M6 16q9 5 18 0m-18 6q9 5 18 0"/>';
    return (
      '<svg width="30" height="36" viewBox="0 0 30 36" fill="rgba(0,191,165,0.22)" stroke="#00bfa5" stroke-width="1.4">' +
      shape +
      "</svg>"
    );
  }
  function presetGeometrySignature(value) {
    const ignored = new Set([
      "name",
      "lang",
      "theme",
      "export_target",
      "auto_configure_slicer",
      "resolution",
    ]);
    return JSON.stringify(
      Object.entries(value)
        .filter(([key]) => !ignored.has(key))
        .sort(([a], [b]) => a.localeCompare(b)),
    );
  }
  function refreshActivePreset() {
    const current = presetGeometrySignature(params),
      all = builtins.concat(userPresets);
    if (
      all.some(
        (item) =>
          item.id === activePreset &&
          presetGeometrySignature(item.params) === current,
      )
    )
      return;
    activePreset =
      all.find((item) => presetGeometrySignature(item.params) === current)
        ?.id || "";
  }
  function renderPresets() {
    refreshActivePreset();
    const grid = $("presets-grid");
    grid.replaceChildren();
    const combined = userPresets
      .map((p) => ({ ...p, user: true }))
      .concat(builtins);
    for (const item of combined) {
      if (presetFilter === "user" && !item.user) continue;
      if (
        !["all", "user"].includes(presetFilter) &&
        item.params.module !== presetFilter
      )
        continue;
      const card = document.createElement("div");
      card.className =
        "preset-card" + (activePreset === item.id ? " active" : "");
      card.dataset.presetId = item.id;
      card.tabIndex = 0;
      card.setAttribute("role", "button");
      const thumb = document.createElement("div");
      thumb.className = "preset-thumb";
      thumb.innerHTML = miniSvg(item.params);
      const meta = document.createElement("div");
      meta.className = "preset-meta";
      const name = document.createElement("div");
      name.className = "preset-name";
      const title = item.user ? item.name : localeText(item.name_en, item.name_pt);
      name.textContent = title;
      name.title = title;
      const sub = document.createElement("div");
      sub.className = "preset-sub";
      sub.textContent = `Ø${item.params.nominal_dia} · P${item.params.pitch} mm`;
      meta.append(name, sub);
      card.append(thumb, meta);
      if (item.user) {
        const remove = document.createElement("button");
        remove.className = "preset-del-btn";
        remove.textContent = "×";
        remove.setAttribute(
          "aria-label",
          localeText("Delete preset", "Excluir preset"),
        );
        remove.onclick = (event) => {
          event.stopPropagation();
          send({ type: "preset_delete", id: item.id });
        };
        card.append(remove);
      }
      const activate = () => {
        activePreset = item.id;
        params = { ...clone(item.params), lang, theme };
        syncControls();
        renderPresets();
        scheduleUpdate();
      };
      card.onclick = activate;
      card.onkeydown = (event) => {
        if (["Enter", " "].includes(event.key)) {
          event.preventDefault();
          activate();
        }
      };
      grid.append(card);
    }
  }
  function translate() {
    document.documentElement.lang = lang;
    document.documentElement.dataset.theme = theme;
    document.documentElement.dir = BOOT_PAYLOAD.languages.find(item => item.code === lang)?.direction || "ltr";
    $("language").value = lang;
    $("language").setAttribute("aria-label", localeText("Language", "Idioma"));
    document.querySelectorAll("[data-locale-title]").forEach(el => el.title = localeText(el.dataset.localeTitle));
    document.querySelectorAll("[data-locale-aria]").forEach(el => el.setAttribute("aria-label", localeText(el.dataset.localeAria)));
    $("inp-save-preset-name").placeholder = localeText("Preset name", "Nome do preset");
    $("lbl-cross-cut").textContent = view.cutPct ? view.cutPct + "%" : localeText("Off", "Desligado");
    $("btn-cut-off").textContent = localeText("Off", "Desligado");
    $("theme").textContent = theme === "dark" ? "☾" : "☀";
    document
      .querySelectorAll("[data-i18n]")
      .forEach((element) => (element.textContent = text(element.dataset.i18n)));
    buildControls();
    renderPresets();
    drawLoupe();
    if (report) renderWarnings();
    if (lastStatus) status(lastStatus.source, lastStatus.error, lastStatus.paths);
    updateHud();
  }
  function renderWarnings() {
      $("warning").hidden = !(currentWarning || report.experimental);
      $("warning").textContent = localeText(currentWarning) || text("experimental");
      $("hud-status-pill").textContent = currentWarning
        ? "⚠"
        : report.experimental
          ? "EXP"
          : "OK";
      $("hud-status-pill").className =
        "hud-status-pill " +
        (currentWarning || report.experimental ? "warn" : "ok");
      $("hud-warnings").textContent =
        currentWarning || report.experimental
          ? localeText(currentWarning) || text("experimental")
          : "";
  }
  function syncHost(newHost) {
    host = { ...newHost };
    $("printer-pill-name").textContent = host.printer_name || "OrcaSlicer";
    $("printer-pill-specs").textContent =
      `· ${host.bed_x || 220}×${host.bed_y || 220}×${host.max_z || 250} mm · ${host.nozzle_mm || 0.4}mm`;
    $("printer-pill").classList.remove("syncing");
    buildGrid();
  }
  function handleHostMessage(raw) {
    let message = raw && raw.data !== undefined ? raw.data : raw;
    if (typeof message === "string") {
      try {
        message = JSON.parse(message);
      } catch {
        return;
      }
    }
    if (!message || typeof message !== "object") return;
    if (message.type === "preferences_updated") {
      if (message.client_id === clientId && message.language_request_id < languageRequest) return;
      if (Number.isFinite(message.language_revision) && message.language_revision < languageRevision) return;
      languageRevision = message.language_revision || languageRevision;
      lang = normalizeLanguage(message.lang);
      params.lang = lang;
      translate();
      return;
    }
    if (message.type === "host_state") {
      syncHost(message.host || {});
      status(
        "Printer synchronized.",
      );
      return;
    }
    if (message.type === "init_state") {
      const initial = resolveInitialState(message, {
        params,
        lang,
        theme,
        host,
        userPresets,
        builtins,
        userOverrodeTheme,
      });
      params = initial.params;
      lang = languageRequest ? lang : normalizeLanguage(initial.lang);
      params.lang = lang;
      theme = initial.theme;
      params.theme = theme;
      userPresets = initial.userPresets;
      builtins = initial.builtins;
      syncHost(initial.host);
      if (initial.acceptDesign) translate();
      else renderPresets();
      return;
    }
    if (message.type === "busy") {
      if (message.busy)
        status("Generating mesh…");
      return;
    }
    if (message.type === "presets_updated") {
      userPresets = message.user_presets;
      renderPresets();
      return;
    }
    if (message.type === "geometry") {
      if (geometryRevisionIsStale(message)) return;
      const acknowledgedRequest = message.client_acknowledgements?.[clientId];
      if (Number.isFinite(acknowledgedRequest))
        acknowledgedRevision = Math.max(
          acknowledgedRevision,
          acknowledgedRequest,
        );
      if (message.client_id === clientId && Number.isFinite(message.request_id))
        acknowledgedRevision = Math.max(
          acknowledgedRevision,
          message.request_id,
        );
      params = { ...message.params, lang };
      params.theme = resolveStudioTheme(
        params.theme,
        host,
        theme,
        userOverrodeTheme,
      );
      if (params.lang !== lang || params.theme !== theme) {
        lang = params.lang;
        theme = params.theme;
        translate();
      }
      syncControls();
      renderPresets();
      profile = message.profile;
      report = message.report;
      uploadMeshes(message.meshes || []);
      $("undo").disabled = !message.can_undo;
      $("redo").disabled = !message.can_redo;
      $("radial").textContent = report.radial_clearance_mm.toFixed(3) + " mm";
      $("lead").textContent = report.lead_mm.toFixed(2) + " mm";
      $("fit-badge").textContent =
        "cᵣ " + report.radial_clearance_mm.toFixed(3) + " mm";
      currentWarning = message.warning || "";
      renderWarnings();
      status(
        message.warning ||
          (params.export_target === "calibration"
            ? words.en.notch
            : "Mesh updated."),
        Boolean(message.warning),
      );
      drawLoupe();
      return;
    }
    if (message.type === "action_result")
      status(
        message.message || "",
        message.ok === false,
        [...(message.detail ? [message.detail] : []), ...(message.paths || [])],
      );
  }
  window.handleHostMessage = handleHostMessage;
  window.addEventListener("message", handleHostMessage);
  if (window.chrome?.webview)
    window.chrome.webview.addEventListener("message", handleHostMessage);
  if (window.orca && typeof window.orca.onMessage === "function")
    window.orca.onMessage(handleHostMessage);
  const MATERIAL_PRESETS = {
    emerald_silk: {
      base: [0.02, 0.72, 0.63],
      saucer: [0.14, 0.24, 0.25],
      rough: 0.22,
      metal: 0.3,
    },
    terracotta: {
      base: [0.79, 0.4, 0.28],
      saucer: [0.68, 0.34, 0.24],
      rough: 0.78,
      metal: 0.02,
    },
    matte_ceramic: {
      base: [0.91, 0.9, 0.87],
      saucer: [0.8, 0.78, 0.74],
      rough: 0.66,
      metal: 0.02,
    },
    copper_bronze: {
      base: [0.76, 0.48, 0.31],
      saucer: [0.36, 0.25, 0.2],
      rough: 0.26,
      metal: 0.72,
    },
    xray: {
      base: [0.04, 0.8, 0.72],
      saucer: [0.16, 0.48, 0.52],
      rough: 0.18,
      metal: 0.15,
    },
    heatmap: {
      base: [0.05, 0.76, 0.45],
      saucer: [0.05, 0.76, 0.45],
      rough: 0.55,
      metal: 0.05,
    },
  };

  const meshVertexSource =
      "#version 300 es\n      precision highp float;\n      in vec3 a_pos;\n      in vec3 a_nrm;\n      in float a_ovh;\n      in float a_part;\n      in float a_role;\n      uniform mat4 u_mvp;\n      uniform mat4 u_model;\n      out vec3 v_pos;\n      out vec3 v_nrm;\n      out float v_ovh;\n      out float v_part;\n      out float v_surfaceRole;\n      void main() {\n        v_pos = (u_model * vec4(a_pos, 1.0)).xyz;\n        v_nrm = mat3(u_model) * a_nrm;\n        v_ovh = a_ovh;\n        v_part = a_part;\n        v_surfaceRole = a_role;\n        gl_Position = u_mvp * vec4(v_pos, 1.0);\n      }\n    ",
    meshFragmentSource =
      "#version 300 es\n      precision highp float;\n      in vec3 v_pos;\n      in vec3 v_nrm;\n      in float v_ovh;\n      in float v_part;\n      in float v_surfaceRole;\n      uniform vec3 u_eye;\n      uniform vec3 u_baseColor;\n      uniform vec3 u_saucerColor;\n      uniform float u_roughness;\n      uniform float u_metallic;\n      uniform float u_heatmap;\n      uniform float u_xrayMode;\n      uniform float u_clipMode;\n      uniform float u_clipVal;\n      uniform float u_passMode;\n      uniform float u_lightTheme;\n      out vec4 outColor;\n\n      vec3 heatmapColor(float deg) {\n        vec3 safeA = vec3(0.02, 0.76, 0.45);\n        vec3 safeB = vec3(0.18, 0.85, 0.42);\n        vec3 warn  = vec3(1.00, 0.68, 0.02);\n        vec3 crit  = vec3(0.98, 0.20, 0.16);\n        if (deg <= 42.0) return mix(safeA, safeB, clamp(deg / 42.0, 0.0, 1.0));\n        if (deg <= 46.0) return mix(safeB, warn, (deg - 42.0) / 4.0);\n        if (deg <= 55.0) return mix(warn, crit, (deg - 46.0) / 9.0);\n        return crit;\n      }\n\n      void main() {\n        float clipRim = 0.0;\n        if (u_clipMode > 0.5 && u_passMode < 0.5) {\n          float dist = (u_clipMode < 1.5) ? (v_pos.y - u_clipVal) : (u_clipVal - v_pos.z);\n          if (dist < 0.0) {\n            discard;\n          }\n          if (dist < 1.45) {\n            clipRim = 1.0 - (dist / 1.45);\n          }\n        } else if (u_clipMode > 0.5 && u_clipMode < 1.5 && u_passMode > 1.5) {\n          if (v_pos.y < u_clipVal) discard;\n        }\n\n        // Special Pass 1: Solid Horizontal Z-Slice CAD Cross-Section Cap\n        if (u_passMode > 0.5 && u_passMode < 1.5) {\n          float hatch = sin((v_pos.x + v_pos.y) * 2.35);\n          vec3 capA = vec3(1.00, 0.76, 0.20);\n          vec3 capB = vec3(0.08, 0.92, 0.80);\n          vec3 cCol = mix(capA, capB, hatch > 0.25 ? 0.65 : 0.12);\n          outColor = vec4(cCol, u_xrayMode > 0.5 ? 0.90 : 1.0);\n          return;\n        }\n\n        // Special Pass 2: Holographic Spiral Mode Top-Cap Indicator Disk\n        if (u_passMode > 1.5) {\n          float r = length(v_pos.xy);\n          float rings = 0.5 + 0.5 * sin(r * 1.45);\n          float diag = step(0.35, fract((v_pos.x - v_pos.y) * 0.14));\n          vec3 holoCol = mix(vec3(1.00, 0.68, 0.18), vec3(0.10, 0.92, 0.82), rings * 0.65);\n          float alpha = 0.18 + 0.20 * diag * rings;\n          outColor = vec4(holoCol, alpha);\n          return;\n        }\n\n        vec3 N = normalize(v_nrm);\n        bool backFace = !gl_FrontFacing;\n        if (backFace) N = -N;\n\n        vec3 V = normalize(u_eye - v_pos);\n        vec3 L1 = normalize(vec3(-0.52, -0.64, 0.56));\n        vec3 L2 = normalize(vec3(0.68, -0.25, 0.42));\n        vec3 L3 = normalize(vec3(0.05, 0.82, 0.35));\n        float diff1 = max(dot(N, L1), 0.0);\n        float diff2 = max(dot(N, L2), 0.0);\n        float diff3 = max(dot(N, L3), 0.0);\n\n        // Two-Pass Translucent X-Ray / Wall Caliper Shader\n        if (u_xrayMode > 0.5) {\n          float ndv = abs(dot(N, V));\n          float fresnel = pow(1.0 - clamp(ndv, 0.0, 1.0), 2.15);\n          vec3 Hx = normalize(L1 + V);\n          float specX = pow(max(dot(N, Hx), 0.0), 54.0) * 0.45;\n\n          vec3 xCol;\n          float xAlpha;\n          if (v_surfaceRole > 0.5 && v_surfaceRole < 1.5) {\n            // Inner cavity wall, inner floor, and drainage holes -> warm glowing amber/coral!\n            bool isFloorPlane = abs(N.z) > 0.68;\n            vec3 innerBase = isFloorPlane ? vec3(1.00, 0.43, 0.18) : vec3(1.00, 0.58, 0.22);\n            if (u_lightTheme > 0.5) innerBase *= 0.88;\n            xCol = innerBase * (0.48 + 0.55 * diff1 + 0.25 * diff2)\n                 + vec3(1.00, 0.84, 0.46) * (fresnel * 0.65 + specX * 0.5);\n            xAlpha = isFloorPlane ? (0.52 + 0.28 * fresnel) : (0.35 + 0.42 * fresnel);\n          } else if (v_surfaceRole >= 1.5) {\n            // Top mouth lip / rim -> crisp luminous cyan-gold ring\n            xCol = vec3(0.28, 0.96, 0.86) * (0.58 + 0.42 * diff1) + vec3(0.85) * specX;\n            xAlpha = 0.62 + 0.28 * fresnel;\n          } else {\n            // Outer wall -> smoky emerald/cyan glass with Fresnel rim glow\n            vec3 glassBase = (u_lightTheme > 0.5) ? vec3(0.00, 0.56, 0.52) : vec3(0.05, 0.82, 0.74);\n            if (v_part > 0.5) glassBase = (u_lightTheme > 0.5) ? vec3(0.22, 0.42, 0.46) : vec3(0.18, 0.55, 0.58);\n            xCol = glassBase * (0.40 + 0.52 * diff1 + 0.22 * diff2)\n                 + vec3(0.46, 0.98, 0.92) * (fresnel * 0.78)\n                 + vec3(1.0) * specX;\n            xAlpha = 0.15 + 0.48 * fresnel + specX * 0.28;\n          }\n\n          if (backFace) xAlpha *= 0.76;\n          if (clipRim > 0.01) {\n            xCol = mix(xCol, vec3(1.00, 0.82, 0.24), clipRim * 0.88);\n            xAlpha = max(xAlpha, 0.94 * clipRim);\n          }\n          outColor = vec4(clamp(xCol, 0.0, 1.0), clamp(xAlpha, 0.08, 0.95));\n          return;\n        }\n\n        // Standard Opaque PBR-Lite Studio Shading\n        vec3 albedo = v_part > 0.5 ? u_saucerColor : u_baseColor;\n        if (u_heatmap > 0.5) {\n          albedo = heatmapColor(v_ovh);\n        } else if (u_clipMode > 0.5 && v_surfaceRole > 0.5 && v_surfaceRole < 1.5) {\n          albedo = mix(albedo, vec3(0.98, 0.58, 0.24), 0.42);\n        } else if (backFace && u_clipMode > 0.5) {\n          albedo = mix(albedo, vec3(1.0, 0.72, 0.28), 0.45);\n        }\n\n        float layerWave = 0.985 + 0.015 * sin(v_pos.z * 31.4159);\n        albedo *= layerWave;\n\n        vec3 H1 = normalize(L1 + V);\n        float shininess = mix(96.0, 14.0, u_roughness);\n        float spec1 = pow(max(dot(N, H1), 0.0), shininess) * mix(0.28, 0.85, 1.0 - u_roughness);\n\n        float hemi = 0.5 + 0.5 * N.z;\n        vec3 ambient = mix(vec3(0.14, 0.16, 0.20), vec3(0.34, 0.37, 0.42), hemi);\n        float rim = pow(1.0 - max(dot(N, V), 0.0), 3.2) * 0.22;\n\n        vec3 specTint = mix(vec3(1.0), albedo, u_metallic);\n        vec3 color = albedo * (ambient + 0.78 * diff1 + 0.32 * diff2 + 0.22 * diff3)\n                   + specTint * spec1\n                   + vec3(0.55, 0.85, 0.80) * rim;\n\n        if (clipRim > 0.01) {\n          color = mix(color, vec3(1.00, 0.80, 0.22), clipRim * 0.85);\n        }\n\n        color = pow(clamp(color, 0.0, 1.0), vec3(0.92));\n        outColor = vec4(color, 1.0);\n      }\n    ",
    lineVertexSource =
      "#version 300 es\n      precision highp float;\n      in vec3 a_pos;\n      uniform mat4 u_mvp;\n      void main() {\n        gl_Position = u_mvp * vec4(a_pos, 1.0);\n      }\n    ",
    lineFragmentSource =
      "#version 300 es\n      precision highp float;\n      uniform vec4 u_color;\n      out vec4 outColor;\n      void main() {\n        outColor = u_color;\n      }\n    ";
  function program(vertexSource, fragmentSource) {
    const result = gl.createProgram();
    for (const [type, source] of [
      [gl.VERTEX_SHADER, vertexSource],
      [gl.FRAGMENT_SHADER, fragmentSource],
    ]) {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS))
        throw Error(gl.getShaderInfoLog(shader));
      gl.attachShader(result, shader);
    }
    gl.linkProgram(result);
    if (!gl.getProgramParameter(result, gl.LINK_STATUS))
      throw Error(gl.getProgramInfoLog(result));
    return result;
  }
  function buffer(data, target = gl.ARRAY_BUFFER) {
    const value = gl.createBuffer();
    gl.bindBuffer(target, value);
    gl.bufferData(target, data, gl.STATIC_DRAW);
    return value;
  }
  function bindAttribute(program, name, value, size) {
    const location = gl.getAttribLocation(program, name);
    if (location < 0) return;
    gl.bindBuffer(gl.ARRAY_BUFFER, value);
    gl.enableVertexAttribArray(location);
    gl.vertexAttribPointer(location, size, gl.FLOAT, false, 0, 0);
  }
  function buildGrid() {
    if (!gl) return;
    const vertices = [],
      width = host.bed_x || 220,
      depth = host.bed_y || 220;
    for (let x = -width / 2; x <= width / 2; x += 10)
      vertices.push(x, -depth / 2, -0.08, x, depth / 2, -0.08);
    for (let y = -depth / 2; y <= depth / 2; y += 10)
      vertices.push(-width / 2, y, -0.08, width / 2, y, -0.08);
    if (gridBuffer) gl.deleteBuffer(gridBuffer);
    gridBuffer = buffer(new Float32Array(vertices));
    gridCount = vertices.length / 3;
  }

  function uploadMeshes(raw) {
    for (const item of meshes)
      if (gl && item.gpu)
        Object.values(item.gpu).forEach((value) => gl.deleteBuffer(value));
    meshes = raw.map((item, partIndex) => {
      const positions = new Float32Array(item.vertices),
        indices = new Uint32Array(item.triangles),
        normals = new Float32Array(positions.length),
        overhang = new Float32Array(positions.length / 3),
        roles = new Float32Array(positions.length / 3),
        parts = new Float32Array(positions.length / 3).fill(partIndex ? 1 : 0),
        wire = new Uint32Array(indices.length * 2);
      let maximum = 0;
      for (let i = 0; i < indices.length; i += 3) {
        const a = indices[i] * 3,
          b = indices[i + 1] * 3,
          c = indices[i + 2] * 3,
          ux = positions[b] - positions[a],
          uy = positions[b + 1] - positions[a + 1],
          uz = positions[b + 2] - positions[a + 2],
          vx = positions[c] - positions[a],
          vy = positions[c + 1] - positions[a + 1],
          vz = positions[c + 2] - positions[a + 2],
          nx = uy * vz - uz * vy,
          ny = uz * vx - ux * vz,
          nz = ux * vy - uy * vx,
          length = Math.hypot(nx, ny, nz) || 1,
          atBed =
            positions[a + 2] < 0.001 &&
            positions[b + 2] < 0.001 &&
            positions[c + 2] < 0.001,
          angle = atBed
            ? 0
            : (Math.asin(Math.max(0, -nz / length)) * 180) / Math.PI;
        maximum = Math.max(maximum, angle);
        for (const vertex of [a, b, c]) {
          normals[vertex] += nx;
          normals[vertex + 1] += ny;
          normals[vertex + 2] += nz;
          overhang[vertex / 3] = Math.max(overhang[vertex / 3], angle);
        }
        wire.set(
          [
            indices[i],
            indices[i + 1],
            indices[i + 1],
            indices[i + 2],
            indices[i + 2],
            indices[i],
          ],
          i * 2,
        );
      }
      for (let i = 0; i < normals.length; i += 3) {
        const length =
          Math.hypot(normals[i], normals[i + 1], normals[i + 2]) || 1;
        normals[i] /= length;
        normals[i + 1] /= length;
        normals[i + 2] /= length;
        roles[i / 3] =
          positions[i] * normals[i] + positions[i + 1] * normals[i + 1] < -0.01
            ? 1
            : Math.abs(normals[i + 2]) > 0.7
              ? 2
              : 0;
      }
      return {
        ...item,
        vertices: positions,
        indices,
        maxOverhang: maximum,
        gpu: gl
          ? {
              pos: buffer(positions),
              nrm: buffer(normals),
              ovh: buffer(overhang),
              part: buffer(parts),
              role: buffer(roles),
              idx: buffer(indices, gl.ELEMENT_ARRAY_BUFFER),
              wire: buffer(wire, gl.ELEMENT_ARRAY_BUFFER),
            }
          : null,
      };
    });
    updateHud();
  }
  function updateHud() {
    const bounds = getSceneBounds();
    $("hud-wall-floor").textContent =
      `${params.wall_thickness.toFixed(1)} / ${params.floor_thickness.toFixed(1)} mm`;
    $("hud-mouth-hole").textContent =
      "Ø " + params.nominal_dia.toFixed(1) + " mm";
    $("hud-dims").textContent = bounds.size.map((x) => x.toFixed(1)).join("×");
    $("hud-overhang").textContent =
      (meshes.length
        ? Math.max(...meshes.map((item) => item.maxOverhang))
        : 0
      ).toFixed(1) + "°";
    $("hud-weight").textContent =
      "~" +
      meshes.reduce((sum, item) => sum + item.volume_cm3 * 1.24, 0).toFixed(1) +
      " g";
    $("hud-tris").textContent = meshes
      .reduce((sum, item) => sum + item.indices.length / 3, 0)
      .toLocaleString();
    const out =
      bounds.size[0] > (host.bed_x || 220) ||
      bounds.size[1] > (host.bed_y || 220) ||
      bounds.size[2] > (host.max_z || 250);
    $("bed-alert-banner").classList.toggle("visible", out);
    $("bed-alert-text").textContent = text("fitPrinter");
  }
  function drawFrame(now) {
    requestAnimationFrame(drawFrame);
    if (!gl || !meshProgram) return;
    const delta = Math.min(0.05, (now - lastFrame) / 1000 || 0);
    lastFrame = now;
    if (view.animate) {
      view.spin = (view.spin + delta * 0.7) % (Math.PI * 4);
      drawLoupe();
    }
    if (view.autoSpin) view.yaw += delta * 0.25;
    const canvas = $("gl-canvas"),
      w = Math.max(1, canvas.clientWidth),
      h = Math.max(1, canvas.clientHeight),
      dpr = Math.min(window.devicePixelRatio || 1, 2);
    if (
      canvas.width !== Math.round(w * dpr) ||
      canvas.height !== Math.round(h * dpr)
    ) {
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
    }
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.depthMask(true);
    gl.enable(gl.DEPTH_TEST);
    gl.disable(gl.CULL_FACE);
    gl.disable(gl.BLEND);
    if (theme === "light") gl.clearColor(0.84, 0.88, 0.92, 1);
    else gl.clearColor(0.095, 0.11, 0.138, 1);
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    const bounds = getSceneBounds(),
      radius = Math.max(5, Math.hypot(...bounds.size) / 2),
      verticalFov = (38 * Math.PI) / 180,
      horizontalFov = 2 * Math.atan((Math.tan(verticalFov / 2) * w) / h),
      distance =
        ((radius / Math.sin(Math.min(verticalFov, horizontalFov) / 2)) * 1.15) /
        view.zoom,
      target = bounds.center,
      cp = Math.cos(view.pitch),
      eye = [
        target[0] + distance * cp * Math.cos(view.yaw),
        target[1] + distance * cp * Math.sin(view.yaw),
        target[2] + distance * Math.sin(view.pitch),
      ],
      mvp = mat4Multiply(
        mat4Perspective(
          verticalFov,
          w / h,
          Math.max(0.1, distance - radius * 2),
          distance + radius * 4 + 100,
        ),
        mat4LookAtZUp(eye, target),
      );
    lastCamera = { mvp, eye, w, h, bounds };
    if (gridBuffer) {
      gl.useProgram(lineProgram);
      gl.uniformMatrix4fv(
        gl.getUniformLocation(lineProgram, "u_mvp"),
        false,
        mvp,
      );
      gl.uniform4fv(
        gl.getUniformLocation(lineProgram, "u_color"),
        theme === "light" ? [0.35, 0.45, 0.52, 0.45] : [0, 0.72, 0.62, 0.34],
      );
      bindAttribute(lineProgram, "a_pos", gridBuffer, 3);
      gl.drawArrays(gl.LINES, 0, gridCount);
    }
    const clipMode = view.cutPct <= 0 ? 0 : view.cutAxis === "y" ? 1 : 2,
      clipValue =
        view.cutAxis === "y"
          ? bounds.min[1] + (bounds.size[1] * view.cutPct) / 100
          : bounds.min[2] + bounds.size[2] * (1 - view.cutPct / 100),
      material =
        MATERIAL_PRESETS[
          view.xray ? "xray" : view.heatmap ? "heatmap" : view.material
        ] || MATERIAL_PRESETS.emerald_silk;
    gl.useProgram(meshProgram);
    gl.uniformMatrix4fv(
      gl.getUniformLocation(meshProgram, "u_mvp"),
      false,
      mvp,
    );
    gl.uniform3fv(gl.getUniformLocation(meshProgram, "u_eye"), eye);
    gl.uniform3fv(
      gl.getUniformLocation(meshProgram, "u_baseColor"),
      material.base,
    );
    gl.uniform3fv(
      gl.getUniformLocation(meshProgram, "u_saucerColor"),
      material.saucer,
    );
    for (const [name, value] of Object.entries({
      u_roughness: material.rough,
      u_metallic: material.metal,
      u_heatmap: view.heatmap && !view.xray ? 1 : 0,
      u_xrayMode: view.xray ? 1 : 0,
      u_clipMode: clipMode,
      u_clipVal: clipValue,
      u_passMode: 0,
      u_lightTheme: theme === "light" ? 1 : 0,
    }))
      gl.uniform1f(gl.getUniformLocation(meshProgram, name), value);
    meshes.forEach((item, index) => {
      if (!item.gpu) return;
      gl.useProgram(meshProgram);
      gl.uniformMatrix4fv(
        gl.getUniformLocation(meshProgram, "u_model"),
        false,
        modelMatrix(index),
      );
      for (const [name, key, size] of [
        ["a_pos", "pos", 3],
        ["a_nrm", "nrm", 3],
        ["a_ovh", "ovh", 1],
        ["a_part", "part", 1],
        ["a_role", "role", 1],
      ])
        bindAttribute(meshProgram, name, item.gpu[key], size);
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, item.gpu.idx);
      if (view.xray) {
        gl.enable(gl.BLEND);
        gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
        gl.depthMask(false);
        gl.enable(gl.CULL_FACE);
        gl.cullFace(gl.FRONT);
        gl.drawElements(gl.TRIANGLES, item.indices.length, gl.UNSIGNED_INT, 0);
        gl.cullFace(gl.BACK);
        gl.drawElements(gl.TRIANGLES, item.indices.length, gl.UNSIGNED_INT, 0);
        gl.disable(gl.CULL_FACE);
        gl.depthMask(true);
        gl.disable(gl.BLEND);
      } else
        gl.drawElements(gl.TRIANGLES, item.indices.length, gl.UNSIGNED_INT, 0);
      if (view.wire) {
        gl.useProgram(lineProgram);
        gl.uniformMatrix4fv(
          gl.getUniformLocation(lineProgram, "u_mvp"),
          false,
          mat4Multiply(mvp, modelMatrix(index)),
        );
        gl.uniform4fv(
          gl.getUniformLocation(lineProgram, "u_color"),
          view.xray ? [0.35, 0.98, 0.9, 0.35] : [0.02, 0.12, 0.14, 0.5],
        );
        bindAttribute(lineProgram, "a_pos", item.gpu.pos, 3);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, item.gpu.wire);
        gl.enable(gl.BLEND);
        gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
        gl.drawElements(gl.LINES, item.indices.length * 2, gl.UNSIGNED_INT, 0);
        gl.disable(gl.BLEND);
      }
    });
    drawCalipers();
    if (view.animate) updateHud();
  }
  function projected(point) {
    if (!lastCamera) return null;
    const m = lastCamera.mvp,
      w = m[3] * point[0] + m[7] * point[1] + m[11] * point[2] + m[15];
    if (w <= 0) return null;
    return [
      (((m[0] * point[0] + m[4] * point[1] + m[8] * point[2] + m[12]) / w) *
        lastCamera.w) /
        2 +
        lastCamera.w / 2,
      lastCamera.h / 2 -
        (((m[1] * point[0] + m[5] * point[1] + m[9] * point[2] + m[13]) / w) *
          lastCamera.h) /
          2,
    ];
  }
  function drawCalipers() {
    const canvas = $("vp-caliper-canvas"),
      w = canvas.clientWidth,
      h = canvas.clientHeight,
      dpr = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, w * dpr);
    canvas.height = Math.max(1, h * dpr);
    const ctx = canvas.getContext("2d");
    ctx.scale(dpr, dpr);
    if (!view.calipers || !lastCamera || !meshes.length) return;
    const b = lastCamera.bounds,
      color = theme === "light" ? "#006b61" : "#80ffea";
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = 1.2;
    ctx.font = "11px Consolas";
    const edges = [
      [b.min, [b.max[0], b.min[1], b.min[2]], b.size[0]],
      [b.min, [b.min[0], b.max[1], b.min[2]], b.size[1]],
      [[b.max[0], b.max[1], b.min[2]], b.max, b.size[2]],
    ];
    for (const [a, c, value] of edges) {
      const p = projected(a),
        q = projected(c);
      if (!p || !q) continue;
      ctx.beginPath();
      ctx.moveTo(...p);
      ctx.lineTo(...q);
      ctx.stroke();
      const label = value.toFixed(1) + " mm",
        x = (p[0] + q[0]) / 2,
        y = (p[1] + q[1]) / 2,
        width = ctx.measureText(label).width + 10;
      ctx.fillStyle =
        theme === "light" ? "rgba(255,255,255,.94)" : "rgba(24,27,33,.94)";
      ctx.fillRect(x - width / 2, y - 15, width, 17);
      ctx.fillStyle = color;
      ctx.fillText(label, x - width / 2 + 5, y - 3);
      for (const point of [p, q]) {
        ctx.beginPath();
        ctx.arc(...point, 2.3, 0, Math.PI * 2);
        ctx.fill();
      }
    }
  }
  function drawLoupe() {
    if (!profile) return;
    const minimum = Math.max(0, params.thread_length / 2 - params.pitch),
      maximum = Math.min(
        params.thread_length,
        params.thread_length / 2 + params.pitch,
      ),
      z = [],
      male = [],
      female = [],
      advance = (view.spin * params.lead) / (2 * Math.PI);
    let interference = false,
      engaged = 0;
    for (let i = 0; i <= 240; i++) {
      const q = minimum + ((maximum - minimum) * i) / 240;
      z.push(q);
      male.push(radialProfile(q, false));
      const local = q - view.opening - advance;
      female.push(
        local >= 0 && local <= params.thread_length
          ? radialProfile(q - view.opening, true)
          : null,
      );
      if (female.at(-1) !== null) {
        engaged++;
        if (female.at(-1) < male.at(-1) - 1e-6) interference = true;
      }
    }
    const message = interference
      ? text("interference")
      : engaged
        ? text("clear")
        : text("noEngagement");
    $("engagement-readout").textContent = message;
    $("dock-engagement").textContent = message;
    $("clearance-readout").textContent =
      `cᵣ ${(params.diametral_clearance / 2).toFixed(3)} · cₐ ${params.axial_clearance.toFixed(3)} mm`;
    for (const id of ["thread-loupe", "thread-loupe-dock"]) {
      const canvas = $(id),
        rect = canvas.getBoundingClientRect();
      if (!rect.width || !rect.height) continue;
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      const ctx = canvas.getContext("2d");
      ctx.scale(dpr, dpr);
      const values = male.concat(female.filter((value) => value !== null)),
        lo = Math.min(...values) - 0.2,
        hi = Math.max(...values) + 0.2,
        w = rect.width,
        h = rect.height;
      ctx.strokeStyle =
        theme === "light" ? "rgba(80,100,120,.16)" : "rgba(255,255,255,.07)";
      for (let x = 10; x < w; x += 24) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
        ctx.stroke();
      }
      for (const [series, color] of [
        [male, theme === "light" ? "#00897b" : "#00bfa5"],
        [
          female,
          interference ? "#ff5252" : theme === "light" ? "#b66a00" : "#ffb74d",
        ],
      ]) {
        ctx.beginPath();
        let started = false;
        series.forEach((value, i) => {
          if (value === null) {
            started = false;
            return;
          }
          const x = 8 + ((w - 16) * (z[i] - minimum)) / (maximum - minimum),
            y = h - 6 - ((h - 12) * (value - lo)) / (hi - lo);
          if (started) ctx.lineTo(x, y);
          else ctx.moveTo(x, y);
          started = true;
        });
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.stroke();
      }
    }
  }

  function toggleView(key, id) {
    view[key] = !view[key];
    $(id).classList.toggle("active", view[key]);
    $(id).setAttribute("aria-pressed", String(view[key]));
  }
  $("undo").onclick = () => sendMutation({ type: "undo" });
  $("redo").onclick = () => sendMutation({ type: "redo" });
  $("randomize").onclick = () => sendMutation({ type: "randomize", params });
  $("reset").onclick = () => sendMutation({ type: "reset" });
  $("language").onchange = () => {
    lang = normalizeLanguage($("language").value);
    params.lang = lang;
    translate();
    send({type: "set_language", lang, client_id: clientId, language_request_id: ++languageRequest});
  };
  $("theme").onclick = () => {
    userOverrodeTheme = true;
    theme = theme === "dark" ? "light" : "dark";
    params.theme = theme;
    translate();
    scheduleUpdate();
  };
  $("printer-pill").onclick = () => {
    $("printer-pill").classList.add("syncing");
    if (!send({ type: "sync_printer" })) status(words.en.local, true);
  };
  $("inp-design-name").onchange = (event) => change("name", event.target.value);
  $("target").onchange = (event) => change("export_target", event.target.value);
  $("btn-toggle-save-preset").onclick = () =>
    $("save-preset-bar").classList.toggle("open");
  $("btn-confirm-save-preset").onclick = () => {
    const name = $("inp-save-preset-name").value.trim() || params.name;
    send({ type: "preset_save", name, params });
    $("save-preset-bar").classList.remove("open");
  };
  document.querySelectorAll(".filter-chip").forEach(
    (chip) =>
      (chip.onclick = () => {
        presetFilter = chip.dataset.cat;
        document
          .querySelectorAll(".filter-chip")
          .forEach((item) => item.classList.toggle("active", item === chip));
        renderPresets();
      }),
  );
  document.querySelectorAll(".dock-tab-btn").forEach(
    (button) =>
      (button.onclick = () => {
        document.body.dataset.dockTab = button.dataset.tab;
        document
          .querySelectorAll(".dock-tab-btn")
          .forEach((item) => item.classList.toggle("active", item === button));
        drawLoupe();
      }),
  );
  $("btn-vp-xray").onclick = () => {
    toggleView("xray", "btn-vp-xray");
    $("xray-legend").classList.toggle("visible", view.xray);
  };
  $("btn-vp-calipers").onclick = () =>
    toggleView("calipers", "btn-vp-calipers");
  $("btn-vp-wire").onclick = () => toggleView("wire", "btn-vp-wire");
  $("btn-vp-heatmap").onclick = () => {
    toggleView("heatmap", "btn-vp-heatmap");
    $("heatmap-legend").classList.toggle("visible", view.heatmap);
  };
  $("btn-vp-spin").onclick = () => toggleView("autoSpin", "btn-vp-spin");
  $("sel-material").onchange = (event) => {
    const value = event.target.value;
    view.xray = value === "xray";
    view.heatmap = value === "heatmap";
    if (!["xray", "heatmap"].includes(value)) view.material = value;
  };
  $("animate").onclick = () => toggleView("animate", "animate");
  $("explode").oninput = (event) => {
    view.opening = Number(event.target.value);
    $("opening-mm").textContent = view.opening + " mm";
    drawLoupe();
    updateHud();
  };
  // The canonical Y-mode button also keeps the legacy Off/50% shortcut.
  $("cut").onclick = () => {
    view.cutAxis = "y";
    view.cutPct = view.cutPct ? 0 : 50;
    $("inp-cross-cut").value = view.cutPct;
    $("lbl-cross-cut").textContent = view.cutPct ? view.cutPct + "%" : localeText("Off", "Desligado");
    $("cut").classList.add("active");
    $("btn-cut-mode-z").classList.remove("active");
  };
  $("inp-cross-cut").oninput = (event) => {
    view.cutPct = Number(event.target.value);
    $("lbl-cross-cut").textContent = view.cutPct ? view.cutPct + "%" : localeText("Off", "Desligado");
  };
  $("btn-cut-mode-z").onclick = () => {
    view.cutAxis = "z";
    $("cut").classList.remove("active");
    $("btn-cut-mode-z").classList.add("active");
  };
  $("btn-cut-half").onclick = () => {
    view.cutPct = 50;
    $("inp-cross-cut").value = 50;
    $("lbl-cross-cut").textContent = "50%";
  };
  $("btn-cut-off").onclick = () => {
    view.cutPct = 0;
    $("inp-cross-cut").value = 0;
    $("lbl-cross-cut").textContent = localeText("Off", "Desligado");
  };
  document.querySelectorAll("[data-cam]").forEach(
    (button) =>
      (button.onclick = () => {
        const camera = button.dataset.cam;
        if (camera === "fit" || camera === "iso") fitCamera();
        else if (camera === "front") {
          view.yaw = -Math.PI / 2;
          view.pitch = 0;
          view.zoom = 1;
        } else if (camera === "top") {
          view.pitch = Math.PI / 2;
          view.zoom = 1;
        } else if (camera === "bottom") {
          view.pitch = -Math.PI / 2;
          view.zoom = 1;
        }
      }),
  );
  document.querySelectorAll("[data-action]").forEach(
    (button) =>
      (button.onclick = () => {
        const action = button.dataset.action;
        if (action === "open_folder") {
          send({ type: "open_exports" });
          return;
        }
        send({
          type: action === "send_to_plater" ? "send_to_plater" : "export_file",
          format: action === "export_stl" ? "stl" : "3mf",
          params,
        });
      }),
  );
  const canvas = $("gl-canvas");
  canvas.onpointerdown = (event) => {
    drag = [event.clientX, event.clientY];
    canvas.setPointerCapture(event.pointerId);
  };
  canvas.onpointermove = (event) => {
    if (!drag) return;
    view.yaw -= (event.clientX - drag[0]) * 0.008;
    view.pitch = Math.max(
      -1.55,
      Math.min(1.55, view.pitch + (event.clientY - drag[1]) * 0.008),
    );
    drag = [event.clientX, event.clientY];
  };
  canvas.onpointerup = () => (drag = null);
  canvas.onwheel = (event) => {
    event.preventDefault();
    view.zoom = Math.max(
      0.25,
      Math.min(4, view.zoom * Math.exp(-event.deltaY * 0.001)),
    );
  };
  document.addEventListener("keydown", (event) => {
    const tag = String(event.target?.tagName || "").toUpperCase();
    if (
      tag === "INPUT" ||
      tag === "TEXTAREA" ||
      event.target?.isContentEditable
    )
      return;
    if (!(event.ctrlKey || event.metaKey)) return;
    const key = event.key.toLowerCase();
    if (key === "z" || key === "y") {
      event.preventDefault();
      sendMutation({ type: key === "y" || event.shiftKey ? "redo" : "undo" });
    }
  });
  window.addEventListener("resize", () => {
    drawLoupe();
  });
  try {
    gl = canvas.getContext("webgl2", {
      antialias: true,
      alpha: false,
      depth: true,
    });
    if (!gl) throw Error("WebGL2 unavailable");
    meshProgram = program(meshVertexSource, meshFragmentSource);
    lineProgram = program(lineVertexSource, lineFragmentSource);
    buildGrid();
    requestAnimationFrame(drawFrame);
  } catch (error) {
    status(String(error), true);
  }
  theme = resolveStudioTheme(theme, host, theme, userOverrodeTheme);
  params.theme = theme;
  translate();
  syncHost(host);
  status(words.en.waiting);
  if (
    !send({
      type: "ready",
      mode: BOOT_PAYLOAD.mode,
      request_id: 0,
      client_id: clientId,
    })
  )
    status(words.en.local, true);
})();
</script></body></html>"""
