"""Offline bilingual WebGL2 studio. Preview uses the exported NumPy triangles."""

from __future__ import annotations
import json
from .schema import DEFAULT_PARAMS
from .presets_catalog import BUILTIN_PRESETS


def get_studio_html(mode="page", initial_context=None):
    context = initial_context or dict(
        params=DEFAULT_PARAMS,
        builtin_presets=BUILTIN_PRESETS,
        user_presets=[],
        lang="pt",
        theme="dark",
    )
    safe = (
        json.dumps(context, ensure_ascii=False)
        .replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    return _HTML.replace("__CONTEXT__", safe).replace("__MODE__", mode)


_HTML = r"""<!doctype html>
<html lang="pt" data-theme="dark">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Orca Thread Studio</title>
    <style>
      :root {
        --bg: #15171b;
        --panel: #1d2026;
        --card: #242830;
        --input: #16181d;
        --line: #313641;
        --text: #eef2f7;
        --muted: #9aa4b4;
        --accent: #00a896;
        --soft: rgba(0, 191, 165, 0.13);
        --view: #171c24;
        --gold: #ffb74d;
        --danger: #ff6868;
        color-scheme: dark;
        font:
          13px "Segoe UI",
          Ubuntu,
          sans-serif;
      }
      [data-theme="light"] {
        --bg: #edf1f6;
        --panel: #fff;
        --card: #f5f7fb;
        --input: #fff;
        --line: #d4dce5;
        --text: #1b222c;
        --muted: #525e6f;
        --accent: #00897b;
        --soft: rgba(0, 137, 123, 0.12);
        --view: #dce3ec;
        color-scheme: light;
      }
      * {
        box-sizing: border-box;
      }
      [hidden] {
        display: none !important;
      }
      body {
        margin: 0;
        background: var(--bg);
        color: var(--text);
        overflow: hidden;
      }
      button,
      select,
      input {
        font: inherit;
        color: inherit;
      }
      button {
        cursor: pointer;
        border: 1px solid var(--line);
        border-radius: 6px;
        background: var(--card);
        padding: 8px 11px;
      }
      button:hover {
        border-color: var(--accent);
      }
      button:focus-visible,
      input:focus-visible,
      select:focus-visible {
        outline: 2px solid var(--accent);
        outline-offset: 2px;
      }
      button:disabled {
        opacity: 0.4;
        cursor: default;
      }
      header {
        height: 68px;
        border-bottom: 1px solid var(--line);
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0 20px;
        background: var(--panel);
      }
      .brandmark {
        height: 36px;
        width: 36px;
        border: 1px solid var(--accent);
        border-radius: 9px;
        color: var(--accent);
        font: bold 23px Consolas;
        text-align: center;
        line-height: 34px;
      }
      h1 {
        font-size: 17px;
        margin: 0;
        letter-spacing: 0.2px;
      }
      .subtitle {
        font-size: 11px;
        color: var(--muted);
        margin-top: 4px;
      }
      .spacer {
        flex: 1;
      }
      .header-actions {
        display: flex;
        gap: 6px;
      }
      .layout {
        display: grid;
        grid-template-columns: 300px minmax(300px, 1fr) 280px;
        height: calc(100vh - 68px);
        gap: 1px;
        background: var(--line);
      }
      aside {
        background: var(--panel);
        overflow: auto;
        padding: 16px;
      }
      .section-title {
        text-transform: uppercase;
        color: var(--muted);
        font-size: 10px;
        letter-spacing: 1.5px;
        margin: 18px 0 12px;
        font-weight: 700;
      }
      .section-title:first-child {
        margin-top: 0;
      }
      label.field {
        display: grid;
        grid-template-columns: 1fr 108px;
        gap: 8px;
        align-items: center;
        margin: 10px 0;
        font-size: 12px;
      }
      label.field span {
        line-height: 1.4;
      }
      input,
      select {
        width: 100%;
        border: 1px solid var(--line);
        background: var(--input);
        border-radius: 5px;
        padding: 7px;
        min-width: 0;
      }
      input[type="checkbox"] {
        width: 18px;
        height: 18px;
        justify-self: end;
        accent-color: var(--accent);
      }
      input[type="range"] {
        accent-color: var(--accent);
        padding: 0;
      }
      select {
        font-size: 12px;
      }
      .group {
        border-top: 1px solid var(--line);
        padding-top: 10px;
        margin-top: 18px;
      }
      .preview {
        background: var(--view);
        display: flex;
        flex-direction: column;
        min-width: 0;
        overflow: hidden;
      }
      .toolbar {
        display: flex;
        gap: 6px;
        align-items: center;
        padding: 10px 12px;
        flex-wrap: wrap;
        border-bottom: 1px solid var(--line);
        background: var(--panel);
      }
      .toolbar button {
        padding: 6px 9px;
        font-size: 11px;
      }
      .view-wrap {
        flex: 1;
        min-height: 200px;
        position: relative;
      }
      #viewport {
        width: 100%;
        height: 100%;
        display: block;
        touch-action: none;
      }
      .hud {
        position: absolute;
        left: 16px;
        top: 16px;
        pointer-events: none;
        font:
          11px Consolas,
          monospace;
        color: var(--muted);
        line-height: 1.8;
      }
      .axis {
        position: absolute;
        bottom: 14px;
        right: 18px;
        font: 11px Consolas;
        color: var(--muted);
      }
      .loupe {
        height: 190px;
        min-height: 150px;
        border-top: 1px solid var(--line);
        background: var(--panel);
        padding: 12px;
        position: relative;
      }
      .loupe-title {
        font-size: 11px;
        color: var(--muted);
        display: flex;
        justify-content: space-between;
      }
      .loupe canvas {
        height: 130px;
        width: 100%;
      }
      .key {
        display: inline-block;
        width: 8px;
        height: 8px;
        margin-right: 5px;
        background: var(--accent);
        border-radius: 50%;
      }
      .key.female {
        background: var(--gold);
      }
      .metric {
        padding: 12px;
        border: 1px solid var(--line);
        border-radius: 8px;
        background: var(--card);
        margin: 8px 0;
      }
      .metric strong {
        font:
          22px Consolas,
          monospace;
        display: block;
        margin: 4px 0;
        color: var(--accent);
      }
      .metric small {
        color: var(--muted);
      }
      .row {
        display: flex;
        gap: 6px;
        margin: 8px 0;
      }
      .row > * {
        flex: 1;
      }
      .primary {
        background: var(--accent);
        color: #fff;
        border-color: var(--accent);
        font-weight: 600;
        width: 100%;
        margin: 9px 0;
        padding: 12px;
      }
      .hint {
        font-size: 11px;
        color: var(--muted);
        line-height: 1.65;
      }
      .warning {
        background: #ffb74d14;
        border: 1px solid #ffb74d66;
        color: var(--gold);
        padding: 10px;
        border-radius: 6px;
        font-size: 11px;
        line-height: 1.6;
        margin: 10px 0;
      }
      .status {
        white-space: pre-wrap;
        overflow-wrap: anywhere;
        padding: 10px;
        font-size: 11px;
        line-height: 1.5;
        border-left: 2px solid var(--accent);
        margin: 10px 0;
        max-height: 180px;
        overflow: auto;
      }
      .status.error {
        border-color: var(--danger);
      }
      .chip {
        padding: 4px 7px;
        background: var(--soft);
        color: var(--accent);
        border-radius: 4px;
        font-size: 10px;
      }
      .docknav {
        display: none;
      }
      .compact .layout {
        display: block;
        overflow: auto;
        height: calc(100vh - 108px);
      }
      .compact header {
        height: 68px;
        padding: 0 10px;
      }
      .compact h1 {
        font-size: 14px;
      }
      .compact .subtitle {
        font-size: 10px;
      }
      .compact .header-actions button {
        padding: 6px;
      }
      .compact .docknav {
        display: flex;
        background: var(--panel);
        height: 40px;
        border-bottom: 1px solid var(--line);
      }
      .docknav button {
        flex: 1;
        border-radius: 0;
        border: 0;
        background: transparent;
      }
      .docknav button.active {
        color: var(--accent);
        border-bottom: 2px solid var(--accent);
      }
      .compact aside,
      .compact .preview {
        display: none;
      }
      .compact [data-tab="controls"] #controls,
      .compact [data-tab="output"] #output {
        display: block;
      }
      .compact [data-tab="preview"] .preview {
        display: flex;
        height: calc(100vh - 108px);
      }
      .compact header .brandmark {
        display: none;
      }
      @media (max-width: 1000px) {
        .layout {
          grid-template-columns: 255px minmax(250px, 1fr) 235px;
        }
        aside {
          padding: 12px;
        }
      }
      @media (prefers-reduced-motion: reduce) {
        * {
          scroll-behavior: auto;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <div class="brandmark">≋</div>
      <div>
        <h1>Orca Thread Studio</h1>
        <div class="subtitle" data-i="subtitle">
          Roscas, potes e adaptadores · projeto paramétrico
        </div>
      </div>
      <div class="spacer"></div>
      <div class="header-actions">
        <button id="reset" data-i="reset">Resetar</button
        ><button id="undo" title="Undo">↶</button
        ><button id="redo" title="Redo">↷</button
        ><button id="theme" aria-label="Theme">◐</button
        ><button id="language">EN</button>
      </div>
    </header>
    <nav class="docknav">
      <button data-view="controls" class="active" data-i="parameters">
        Parâmetros</button
      ><button data-view="preview" data-i="preview">Visualização</button
      ><button data-view="output" data-i="output">Exportação</button>
    </nav>
    <main class="layout" data-tab="controls">
      <aside id="controls">
        <div class="section-title" data-i="presets">Biblioteca de projetos</div>
        <select id="preset" aria-label="Preset"></select>
        <div class="row">
          <button id="save" data-i="save">Salvar preset</button
          ><button id="remove" data-i="remove">Excluir</button>
        </div>
        <div class="group">
          <div class="section-title" data-i="parameters">Parâmetros</div>
          <div id="fields"></div>
        </div>
      </aside>
      <section class="preview">
        <div class="toolbar">
          <span class="chip">WebGL2 · mm</span
          ><button id="fit" data-i="fit">Enquadrar</button
          ><button id="cut" data-i="cut">Corte axial</button
          ><button id="animate" data-i="animate">Rosquear</button
          ><span class="spacer"></span
          ><label class="hint"
            ><span data-i="explode">Abertura</span>
            <input
              id="explode"
              aria-label="Opening"
              type="range"
              min="0"
              max="40"
              value="12"
              style="width: 95px"
          /></label>
        </div>
        <div class="view-wrap">
          <canvas id="viewport" aria-label="3D model preview"></canvas>
          <div class="hud" id="hud"></div>
          <div class="axis">X · Y · Z ↑</div>
        </div>
        <div class="loupe">
          <div class="loupe-title">
            <span data-i="loupe">Lupa de flancos · seção axial</span
            ><span
              ><i class="key"></i><span data-i="male">Macho</span>
              <i class="key female"></i><span data-i="female">Fêmea</span></span
            >
          </div>
          <canvas id="loupe" aria-label="Thread engagement section"></canvas>
        </div>
      </section>
      <aside id="output">
        <div class="section-title" data-i="analysis">Análise de encaixe</div>
        <div class="metric">
          <small data-i="radial">Folga radial nominal</small
          ><strong id="radial">—</strong><small id="axial">—</small>
        </div>
        <div class="metric">
          <small data-i="lead">Avanço por volta</small
          ><strong id="lead">—</strong><small id="check">—</small>
        </div>
        <div id="warning" class="warning" hidden></div>
        <p class="hint" data-i="physical">
          O encaixe depende do filamento e da impressora. Imprima o calibrador
          antes da peça final.
        </p>
        <div class="section-title" data-i="output">Exportação</div>
        <label class="field"
          ><span data-i="target">Peças</span
          ><select id="target"></select></label
        ><button id="send" class="primary" data-i="send">
          Enviar para a mesa
        </button>
        <div class="row">
          <button id="stl">STL</button><button id="three">3MF</button>
        </div>
        <button id="folder" style="width: 100%" data-i="folder">
          Abrir pasta de exportações
        </button>
        <div id="status" class="status" role="status" aria-live="polite"></div>
        <div class="section-title" data-i="printer">Impressora conectada</div>
        <p id="host" class="hint"></p>
        <p class="hint" data-i="settings">
          3MF: 5 paredes, 5 camadas de topo/base e camada fina para as roscas.
          As peças são distribuídas sem alterar a escala.
        </p>
      </aside>
    </main>
    <script>
      "use strict";
      const INITIAL = __CONTEXT__,
        MODE = "__MODE__";
      let params = { ...INITIAL.params },
        lang = INITIAL.lang === "en" ? "en" : "pt",
        meshes = [],
        profile = null,
        report = null,
        userPresets = INITIAL.user_presets || [],
        builtins = INITIAL.builtin_presets || [],
        cut = false,
        animating = false,
        spin = 0,
        yaw = -0.65,
        pitch = -0.5,
        zoom = 1,
        opening = 12,
        drag = null,
        frameTime = 0;
      const $ = (id) => document.getElementById(id);
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
        diametral_clearance: [
          "Folga diametral · mm",
          "Diametral clearance · mm",
        ],
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
      function text(key) {
        return words[lang][key] || key;
      }
      function optionFill(el, rows, value) {
        el.replaceChildren();
        rows.forEach((row) => {
          const opt = document.createElement("option");
          opt.value = row[0];
          opt.textContent = row[lang === "pt" ? 1 : 2];
          el.append(opt);
        });
        el.value = String(value);
      }
      function buildFields() {
        const box = $("fields");
        box.replaceChildren();
        Object.keys(labels).forEach((key) => {
          const row = document.createElement("label");
          row.className = "field";
          row.dataset.field = key;
          const title = document.createElement("span");
          title.textContent = labels[key][lang === "pt" ? 0 : 1];
          const input = document.createElement(
            options[key] ? "select" : "input",
          );
          input.dataset.key = key;
          if (options[key]) optionFill(input, options[key], params[key]);
          else if (typeof params[key] === "boolean") {
            input.type = "checkbox";
            input.checked = params[key];
          } else {
            input.type = typeof params[key] === "number" ? "number" : "text";
            input.value = params[key];
            if (ranges[key]) {
              input.min = ranges[key][0];
              input.max = ranges[key][1];
              input.step = ranges[key][2];
            } else if (input.type === "number") input.step = ".1";
          }
          input.addEventListener("change", () => {
            params[key] =
              input.type === "checkbox"
                ? input.checked
                : input.type === "number" || key === "starts"
                  ? Number(input.value)
                  : input.value;
            refreshVisibility();
            scheduleUpdate();
          });
          row.append(title, input);
          box.append(row);
        });
        refreshVisibility();
      }
      function refreshVisibility() {
        const mod = params.module,
          standard = mod === "standard_bottle_cap",
          adapter = mod === "hose_vacuum_adapter",
          bolt = mod === "bolt_nut_knob";
        document.querySelectorAll("[data-field]").forEach((row) => {
          const k = row.dataset.field;
          let show = true;
          if (["part"].includes(k)) show = standard;
          if (["diameter", "height"].includes(k))
            show = mod === "container_and_lid";
          if (["head", "head_height", "bore_diameter"].includes(k)) show = bolt;
          if (
            [
              "inlet_diameter",
              "outlet_diameter",
              "adapter_length",
              "end_length",
              "end_a",
              "end_b",
            ].includes(k)
          )
            show = adapter;
          if (k.startsWith("measured_") || k === "measurements_confirmed")
            show = standard && params.standard === "mason_86";
          row.hidden = !show;
          const input = row.querySelector("input,select");
          if (["nominal_dia", "pitch", "thread_length", "starts"].includes(k))
            input.disabled =
              standard && ["pco1881", "mason_70"].includes(params.standard);
        });
      }
      function syncFields() {
        document.querySelectorAll("[data-key]").forEach((el) => {
          if (el.type === "checkbox") el.checked = params[el.dataset.key];
          else el.value = params[el.dataset.key];
        });
        $("target").value = params.export_target;
        refreshVisibility();
      }
      function rebuildPresets() {
        const el = $("preset");
        el.replaceChildren();
        const empty = document.createElement("option");
        empty.value = "";
        empty.textContent =
          lang === "pt" ? "Selecionar projeto…" : "Choose project…";
        el.append(empty);
        builtins.forEach((p) => {
          let o = document.createElement("option");
          o.value = p.id;
          o.textContent = lang === "pt" ? p.name_pt : p.name_en;
          el.append(o);
        });
        userPresets.forEach((p) => {
          let o = document.createElement("option");
          o.value = "user:" + p.id;
          o.textContent = "★ " + p.name;
          el.append(o);
        });
      }
      function translate() {
        document.documentElement.lang = lang;
        document
          .querySelectorAll("[data-i]")
          .forEach((el) => (el.textContent = text(el.dataset.i)));
        $("language").textContent = lang === "pt" ? "EN" : "PT";
        buildFields();
        rebuildPresets();
        optionFill($("target"), options.export_target, params.export_target);
        drawLoupe();
      }
      function status(message, error = false) {
        $("status").textContent = message;
        $("status").classList.toggle("error", error);
      }
      function send(payload) {
        try {
          if (window.orca && typeof window.orca.postMessage === "function") {
            window.orca.postMessage(payload);
            return true;
          }
          if (window.chrome && window.chrome.webview) {
            window.chrome.webview.postMessage(payload);
            return true;
          }
        } catch (e) {
          status(String(e), true);
        }
        return false;
      }
      let updateTimer;
      function scheduleUpdate() {
        clearTimeout(updateTimer);
        updateTimer = setTimeout(() => {
          if (!send({ type: "update", params })) status(text("local"), true);
        }, 180);
      }
      function handleHostMessage(raw) {
        let data = raw && raw.data !== undefined ? raw.data : raw;
        if (typeof data === "string") {
          try {
            data = JSON.parse(data);
          } catch (e) {
            return;
          }
        }
        if (!data || typeof data !== "object") return;
        if (data.type === "init_state") {
          params = { ...data.params };
          userPresets = data.user_presets || userPresets;
          builtins = data.builtin_presets || builtins;
          const host = data.host || {};
          $("host").textContent = [
            host.printer_name,
            host.process_name,
            host.filament_name,
            host.bed_x &&
              `${host.bed_x} × ${host.bed_y} mm · Ø${host.nozzle_mm}`,
          ]
            .filter(Boolean)
            .join("\n");
          translate();
          return;
        }
        if (data.type === "busy") {
          status(
            data.busy
              ? lang === "pt"
                ? "Gerando malha…"
                : "Generating mesh…"
              : "",
          );
          return;
        }
        if (data.type === "presets_updated") {
          userPresets = data.user_presets;
          rebuildPresets();
          return;
        }
        if (data.type === "geometry") {
          params = { ...data.params };
          if (params.lang !== lang || document.documentElement.dataset.theme !== params.theme) {
            lang = params.lang;
            document.documentElement.dataset.theme = params.theme;
            translate();
          }
          syncFields();
          profile = data.profile;
          report = data.report;
          uploadMeshes(data.meshes || []);
          $("undo").disabled = !data.can_undo;
          $("redo").disabled = !data.can_redo;
          $("radial").textContent =
            report.radial_clearance_mm.toFixed(3) + " mm";
          $("axial").textContent =
            (lang === "pt" ? "Folga axial: " : "Axial clearance: ") +
            report.axial_clearance_mm.toFixed(3) +
            " mm";
          $("lead").textContent = report.lead_mm.toFixed(2) + " mm";
          $("check").textContent = report.interference
            ? "INTERFERENCE"
            : text("clear");
          $("warning").hidden = !(data.warning || report.experimental);
          $("warning").textContent = data.warning || text("experimental");
          $("hud").textContent = meshes
            .map(
              (m) =>
                `${m.name} · ${(m.indices.length / 3).toLocaleString()} △ · ${m.volume.toFixed(2)} cm³`,
            )
            .join("\n");
          if (params.export_target === "calibration") status(text("notch"));
          drawLoupe();
          return;
        }
        if (data.type === "action_result") {
          status(
            (data.message || "") +
              (data.paths && data.paths.length
                ? "\n" + data.paths.join("\n")
                : ""),
            data.ok === false,
          );
        }
      }
      window.handleHostMessage = handleHostMessage;
      window.addEventListener("message", handleHostMessage);
      if (window.chrome && window.chrome.webview)
        window.chrome.webview.addEventListener("message", handleHostMessage);
      if (window.orca && typeof window.orca.onMessage === "function")
        window.orca.onMessage(handleHostMessage);
      const canvas = $("viewport"),
        gl = canvas.getContext("webgl2", { antialias: true, alpha: false });
      let program,
        loc = {};
      function shader(type, code) {
        const s = gl.createShader(type);
        gl.shaderSource(s, code);
        gl.compileShader(s);
        if (!gl.getShaderParameter(s, gl.COMPILE_STATUS))
          throw Error(gl.getShaderInfoLog(s));
        return s;
      }
      if (gl) {
        try {
          program = gl.createProgram();
          gl.attachShader(
            program,
            shader(
              gl.VERTEX_SHADER,
              `#version 300 es
precision highp float;in vec3 aPosition;uniform vec3 center;uniform vec3 offset;uniform float scale;uniform float aspect;uniform float yaw;uniform float pitch;uniform float spin;uniform bool invert;out vec3 world;out vec3 eye;void main(){vec3 p=aPosition;if(invert)p.yz=-p.yz;float cs=cos(spin),sn=sin(spin);p.xy=mat2(cs,sn,-sn,cs)*p.xy;p+=offset;world=p; p=(p-center)*scale;float cy=cos(yaw),sy=sin(yaw),cp=cos(pitch),sp=sin(pitch);p.xy=mat2(cy,sy,-sy,cy)*p.xy;vec3 e=vec3(p.x,cp*p.z-sp*p.y,sp*p.z+cp*p.y);eye=e;gl_Position=vec4(e.x/aspect,e.y,e.z*.12,1.);}`,
            ),
          );
          gl.attachShader(
            program,
            shader(
              gl.FRAGMENT_SHADER,
              `#version 300 es
precision highp float;in vec3 world;in vec3 eye;uniform vec3 color;uniform bool clipping;out vec4 frag;void main(){if(clipping&&world.y<0.)discard;vec3 normal=normalize(cross(dFdx(eye),dFdy(eye)));float light=.38+.62*abs(dot(normal,normalize(vec3(-.5,.7,1.))));frag=vec4(color*light,1.);}`,
            ),
          );
          gl.linkProgram(program);
          if (!gl.getProgramParameter(program, gl.LINK_STATUS))
            throw Error(gl.getProgramInfoLog(program));
          gl.useProgram(program);
          [
            "center",
            "offset",
            "scale",
            "aspect",
            "yaw",
            "pitch",
            "spin",
            "invert",
            "color",
            "clipping",
          ].forEach((k) => (loc[k] = gl.getUniformLocation(program, k)));
          loc.position = gl.getAttribLocation(program, "aPosition");
          gl.enable(gl.DEPTH_TEST);
        } catch (e) {
          status(String(e), true);
        }
      } else status("WebGL2 unavailable", true);
      function uploadMeshes(raw) {
        meshes.forEach((m) => {
          if (gl) {
            gl.deleteBuffer(m.vertex);
            gl.deleteBuffer(m.index);
          }
        });
        meshes = raw.map((m) => {
          let vertices = new Float32Array(m.vertices),
            indices = new Uint32Array(m.triangles),
            vertex,
            index;
          if (gl) {
            vertex = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, vertex);
            gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
            index = gl.createBuffer();
            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, index);
            gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);
          }
          return {
            name: m.name,
            vertices,
            indices,
            vertex,
            index,
            volume: m.volume_cm3,
            bounds: m.bounds,
          };
        });
      }
      function draw(now) {
        requestAnimationFrame(draw);
        if (!gl || !program) return;
        const rect = canvas.getBoundingClientRect(),
          dpr = Math.min(window.devicePixelRatio || 1, 2),
          w = Math.max(1, Math.round(rect.width * dpr)),
          h = Math.max(1, Math.round(rect.height * dpr));
        if (canvas.width !== w || canvas.height !== h) {
          canvas.width = w;
          canvas.height = h;
        }
        gl.viewport(0, 0, w, h);
        const light = document.documentElement.dataset.theme === "light";
        gl.clearColor(
          ...(light ? [0.83, 0.87, 0.92, 1] : [0.08, 0.1, 0.13, 1]),
        );
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        if (!meshes.length) return;
        const dt = Math.min(0.05, (now - frameTime) / 1000 || 0);
        frameTime = now;
        if (animating) {
          spin = (spin + dt * 0.7) % (Math.PI * 4);
          drawLoupe();
        }
        let dia = Math.max(
            ...meshes.map((m) => Math.max(m.bounds.size[0], m.bounds.size[1])),
          ),
          top = Math.max(...meshes.map((m) => m.bounds.size[2])),
          pair =
            meshes.length === 2 &&
            params.export_target === "all" &&
            ["container_and_lid", "bolt_nut_knob"].includes(params.module);
        if (pair)
          top += params.thread_length + opening + params.floor_thickness + 15;
        const radialKit = params.export_target === "calibration",
          extent = radialKit ? dia * 3.5 : dia * 1.5,
          size = Math.max(top, extent);
        gl.uniform3f(loc.center, 0, 0, top * 0.48);
        gl.uniform1f(loc.scale, (1.65 * zoom) / size);
        gl.uniform1f(loc.aspect, w / h);
        gl.uniform1f(loc.yaw, yaw);
        gl.uniform1f(loc.pitch, pitch);
        gl.uniform1i(loc.clipping, cut);
        meshes.forEach((m, i) => {
          gl.bindBuffer(gl.ARRAY_BUFFER, m.vertex);
          gl.enableVertexAttribArray(loc.position);
          gl.vertexAttribPointer(loc.position, 3, gl.FLOAT, false, 0, 0);
          gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, m.index);
          let z = 0,
            x = 0,
            invert = false,
            rotation = 0;
          if (pair && i === 1) {
            invert = true;
            rotation = spin * (params.hand === "left" ? -1 : 1);
            z =
              (params.module === "container_and_lid"
                ? params.height + params.floor_thickness
                : params.head_height + params.thread_length) +
              opening +
              (spin / (2 * Math.PI)) * params.lead;
          } else if (meshes.length > 1 && !pair)
            x = (i - (meshes.length - 1) / 2) * dia * 1.15;
          gl.uniform3f(loc.offset, x, 0, z);
          gl.uniform1f(loc.spin, rotation);
          gl.uniform1i(loc.invert, invert);
          gl.uniform3f(
            loc.color,
            ...(i === 1 ? [0.98, 0.64, 0.26] : [0.0, 0.72, 0.61]),
          );
          gl.drawElements(gl.TRIANGLES, m.indices.length, gl.UNSIGNED_INT, 0);
        });
      }
      function radialProfile(q, female) {
        const p = params,
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
              p.standard === "iso_metric"
                ? 0.0625 + 0.61343 / Math.sqrt(3)
                : 0.5;
          return Math.max(
            0,
            Math.min(
              1,
              (root - Math.max(0, Math.abs(q) - widen)) / (root - crest),
            ),
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
      function drawLoupe() {
        const c = $("loupe"),
          rect = c.getBoundingClientRect(),
          dpr = window.devicePixelRatio || 1;
        c.width = Math.max(1, rect.width * dpr);
        c.height = Math.max(1, rect.height * dpr);
        const ctx = c.getContext("2d");
        ctx.scale(dpr, dpr);
        const w = rect.width,
          h = rect.height;
        ctx.clearRect(0, 0, w, h);
        if (!profile) return;
        const center = params.thread_length / 2,
          minimum = Math.max(0, center - params.pitch),
          maximum = Math.min(params.thread_length, center + params.pitch),
          z = [],
          male = [],
          female = [],
          advance = (spin / (2 * Math.PI)) * params.lead;
        let interference = false,
          engaged = 0;
        for (let j = 0; j <= 240; j++) {
          const q = minimum + ((maximum - minimum) * j) / 240;
          z.push(q);
          male.push(radialProfile(q, false));
          const local = q - opening - advance;
          female.push(
            local >= 0 && local <= params.thread_length
              ? radialProfile(q - opening, true)
              : null,
          );
          if (female.at(-1) !== null) {
            engaged++;
            if (female.at(-1) < male.at(-1) - 1e-6) interference = true;
          }
        }
        const all = male.concat(female.filter((v) => v !== null)),
          lo = Math.min(...all) - 0.3,
          hi = Math.max(...all) + 0.3;
        const point = (i, values) => [
          15 + ((w - 30) * (z[i] - minimum)) / (maximum - minimum),
          h - 20 - ((h - 35) * (values[i] - lo)) / (hi - lo),
        ];
        ctx.strokeStyle = getComputedStyle(
          document.documentElement,
        ).getPropertyValue("--line");
        ctx.lineWidth = 1;
        for (let x = 20; x < w; x += 25) {
          ctx.beginPath();
          ctx.moveTo(x, 10);
          ctx.lineTo(x, h - 15);
          ctx.stroke();
        }
        [
          [male, "#00bfa5"],
          [female, interference ? "#ff6868" : "#ffb74d"],
        ].forEach(([values, color]) => {
          ctx.beginPath();
          let started = false;
          values.forEach((v, i) => {
            if (v === null) {
              started = false;
              return;
            }
            const q = point(i, values);
            started ? ctx.lineTo(...q) : ctx.moveTo(...q);
            started = true;
          });
          ctx.strokeStyle = color;
          ctx.lineWidth = 2;
          ctx.stroke();
        });
        ctx.fillStyle = getComputedStyle(
          document.documentElement,
        ).getPropertyValue("--muted");
        ctx.font = "10px Consolas";
        ctx.fillText(
          `z · ${params.pitch.toFixed(2)} mm     cᵣ = ${(params.diametral_clearance / 2).toFixed(3)} · cₐ = ${params.axial_clearance.toFixed(3)} mm`,
          15,
          h - 3,
        );
        $("check").textContent = interference
          ? lang === "pt"
            ? "Interferência nesta posição"
            : "Interference at this position"
          : engaged
            ? text("clear")
            : lang === "pt"
              ? "Tampa fora da região de engate"
              : "Lid outside engagement region";
      }
      canvas.addEventListener("pointerdown", (e) => {
        drag = [e.clientX, e.clientY];
        canvas.setPointerCapture(e.pointerId);
      });
      canvas.addEventListener("pointermove", (e) => {
        if (!drag) return;
        yaw += (e.clientX - drag[0]) * 0.008;
        pitch = Math.max(
          -1.4,
          Math.min(1.4, pitch + (e.clientY - drag[1]) * 0.008),
        );
        drag = [e.clientX, e.clientY];
      });
      canvas.addEventListener("pointerup", () => (drag = null));
      canvas.addEventListener(
        "wheel",
        (e) => {
          e.preventDefault();
          zoom = Math.max(0.3, Math.min(4, zoom * Math.exp(-e.deltaY * 0.001)));
        },
        { passive: false },
      );
      $("fit").onclick = () => {
        yaw = -0.65;
        pitch = -0.5;
        zoom = 1;
        spin = 0;
      };
      $("cut").onclick = () => {
        cut = !cut;
        $("cut").setAttribute("aria-pressed", cut);
      };
      $("animate").onclick = () => {
        animating = !animating;
        $("animate").setAttribute("aria-pressed", animating);
      };
      $("explode").oninput = (e) => {
        opening = Number(e.target.value);
        drawLoupe();
      };
      $("reset").onclick = () => send({ type: "reset" });
      $("undo").onclick = () => send({ type: "undo" });
      $("redo").onclick = () => send({ type: "redo" });
      $("theme").onclick = () => {
        document.documentElement.dataset.theme =
          document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        params.theme = document.documentElement.dataset.theme;
        drawLoupe();
        scheduleUpdate();
      };
      $("language").onclick = () => {
        lang = lang === "pt" ? "en" : "pt";
        params.lang = lang;
        translate();
        scheduleUpdate();
      };
      $("preset").onchange = (e) => {
        let value = e.target.value;
        let preset = value.startsWith("user:")
          ? userPresets.find((p) => p.id === value.slice(5))
          : builtins.find((p) => p.id === value);
        if (preset) {
          params = { ...preset.params };
          syncFields();
          scheduleUpdate();
        }
      };
      $("save").onclick = () => {
        const name = window.prompt(
          lang === "pt" ? "Nome do preset" : "Preset name",
          params.name,
        );
        if (name) send({ type: "preset_save", name, params });
      };
      $("remove").onclick = () => {
        const value = $("preset").value;
        if (value.startsWith("user:"))
          send({ type: "preset_delete", id: value.slice(5) });
      };
      $("target").onchange = (e) => {
        params.export_target = e.target.value;
        scheduleUpdate();
      };
      $("stl").onclick = () =>
        send({ type: "export_file", params, format: "stl" });
      $("three").onclick = () =>
        send({ type: "export_file", params, format: "3mf" });
      $("send").onclick = () =>
        send({ type: "send_to_plater", params, format: "3mf" });
      $("folder").onclick = () => send({ type: "open_exports" });
      document.querySelectorAll("[data-view]").forEach(
        (el) =>
          (el.onclick = () => {
            document.querySelector("main").dataset.tab = el.dataset.view;
            document
              .querySelectorAll("[data-view]")
              .forEach((e) => e.classList.toggle("active", e === el));
            drawLoupe();
          }),
      );
      window.addEventListener("resize", () => {
        document.body.classList.toggle("compact", MODE === "dock" || window.innerWidth < 760);
        drawLoupe();
      });
      if (MODE === "dock" || window.innerWidth < 760)
        document.body.classList.add("compact");
      document.documentElement.dataset.theme =
        INITIAL.theme === "light" ? "light" : "dark";
      translate();
      status(text("waiting"));
      requestAnimationFrame(draw);
      if (!send({ type: "ready", mode: MODE })) status(text("local"), true);
    </script>
  </body>
</html>
"""
