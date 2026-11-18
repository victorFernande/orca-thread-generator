# Orca Thread, Bottle & Adapter Studio (`orca-thread-generator`) — Plano de Implementação Técnica

> **Instrução para a IA que assumir este projeto:**
> Este documento contém a especificação técnica completa, decisões de design alinhadas e o roteiro passo a passo para implementar o plugin nativo **Orca Thread, Bottle & Adapter Studio** para o **OrcaSlicer 2.5.1+**.
> Use como referência obrigatória os projetos irmãos existentes na pasta:
> - `d:\Projects\orca-gear-generator`
> - `d:\Projects\orca-vase-generator`
> Mantenha 100% de paridade com os padrões de arquitetura, empacotamento e testes desses projetos.

---

## 1. Visão Geral & Escopo

- **Nome do Plugin:** `Orca Thread Studio` / `Orca Thread, Bottle & Adapter Studio`
- **Slug / Diretório:** `d:\Projects\orca-thread-generator`
- **ID do Plugin (`[tool.orcaslicer.plugin].id`):** `orca-thread-studio`
- **Nome do Módulo Python:** `thread_studio`
- **Target OS:** Windows (`win32`), macOS (`darwin` arm64/x86_64) e Linux.
- **Ambiente de Execução:** Python `>=3.12` embutido do OrcaSlicer (`C:\Program Files\OrcaSlicer\python\python.exe`) com `numpy>=1.26`. Zero dependências compiladas externas (100% offline).

---

## 2. Decisões de Design (Aprovadas)

1. **4 Módulos Construtivos de Peça:**
   - **`container_and_lid`:** Potes cilíndricos/facetados/recartilhados (*knurled*) com tampa rosqueada casada e canal para anel de vedação.
   - **`standard_bottle_cap`:** Tampas avulsas ou gargalos rosqueados compatíveis com padrões universais:
     - Garrafa PET **PCO-1881** (`Ø28 mm`).
     - Potes de conserva **Mason Jar** (70 mm Regular e 86 mm Boca Larga).
     - Roscas métricas ISO **M6 a M100** (passo padrão e fino).
     - Rosca trapezoidal/45° autossuportada otimizada para impressão FDM sem suportes.
   - **`hose_vacuum_adapter`:** Adaptadores de aspiração de oficina e conexões de mangueira:
     - Transição cônica contínua entre dois diâmetros arbitrários (ex.: `Ø35 mm` para `Ø58 mm`).
     - Pontas configuráveis: encaixe liso cônico por atrito, espigão de mangueira (*hose barb*) ou rosca macho/fêmea.
   - **`bolt_nut_knob`:** Parafusos e porcas mecânicos métricos/trapezoidais com opções de cabeça: sextavada, cilíndrica recartilhada ou manípulo tipo borboleta (*wingnut/thumb knob*).

2. **Entrada Suave Higbee (*Blunt Start*):**
   - Rampa cônica de desbaste gradual na primeira e última espira da rosca, eliminando cristas finas que soltam fios e prevenindo o travamento inicial por encaixe cruzado (*cross-threading*).

3. **Lupa 2D de Engajamento de Rosca (Sincronizada em 60 FPS):**
   - Visualização 2D em corte transversal dos flancos macho e fêmea acoplados.
   - Indicador dinâmico de folga radial ($c_r$) e folga axial ($c_a$), destacando em tempo real qualquer ponto de interferência física ou travamento.

4. **Kit Rápido Calibrador de Rosca (~6 min de impressão):**
   - Gera um conjunto compacto de 3 anéis-teste finos com variações progressivas de folga (ex.: `+0.10 mm`, `+0.18 mm`, `+0.26 mm`) com entalhes de marcação `1..3` para calibrar o filamento na peça real antes de imprimir o modelo final.

5. **Presets:** 12 presets curados bilíngues prontos para impressão (tampas de reposição, adaptadores de aspirador de oficina, potes EDC estanques e parafusos de aperto manual).

---

## 3. Estrutura de Arquivos do Projeto

```text
d:\Projects\orca-thread-generator/
├── pyproject.toml                     # Configuração de empacotamento e metadados do OrcaSlicer
├── README.md                          # Manual completo de uso e apresentação
├── LICENSE                            # Licença MIT
├── .gitignore                         # Exclusão de caches e temporários
├── .gitattributes                     # Normalização LF e marcação de binários
├── assets/
│   ├── icon.svg                       # Ícone vetorial da aba (64x64)
│   ├── icon.png                       # Ícone renderizado para marketplace
│   └── icon.jpg                       # Arte de apresentação do estúdio
├── docs/
│   ├── MANUAL_PT-BR.md                # Manual passo a passo em Português
│   ├── MANUAL_EN.md                   # Manual passo a passo em Inglês
│   └── COMMUNITY_LISTING.md           # Textos prontos para GitHub, Reddit e OrcaCloud
├── scripts/
│   └── build_and_install.py           # Empacotador AST PEP 723 single-file + instalador local
├── src/
│   └── thread_studio/
│       ├── __init__.py                # Exportações do pacote
│       ├── schema.py                  # Dataclasses de parâmetros e normalização segura
│       ├── thread_math.py             # Matemática ISO 68-1, perfis FDM 45°, Higbee e engajamento
│       ├── mesh_generator.py          # Motor geométrico NumPy 100% 2-manifold estanque
│       ├── exporters.py               # STL binário + OrcaSlicer 3MF multi-objeto com layout 2D
│       ├── presets_catalog.py         # 12 presets curados + persistência JSON do usuário
│       ├── studio_ui.py               # Interface HTML5 + WebGL2 60 FPS + Lupa 2D de flancos
│       ├── plugin_main.py             # Bridge nativa @orca.plugin (Pages + Script Dock + IPC WM_COPYDATA)
│       └── icon.svg                   # Cópia do ícone para auto-materialização
├── dist/
│   ├── orca_thread_generator.py       # Bundle único PEP 723 com icon.svg auto-materializado
│   ├── orca_thread_generator_any.py   # Bundle universal para OrcaCloud
│   └── orca_thread_generator-1.0.0-py3-none-any.whl
└── tests/
    ├── test_thread_math_and_clearance.py # Testes de matemática de roscas e entrada Higbee
    ├── test_geometry_manifold.py      # Testes de topologia estanque (Euler-Poincaré, normais)
    └── test_exporters_and_bridge.py   # Testes de 3MF, STL, PEP 723 e bridge nativo
```

---

## 4. Requisitos de Implementação por Módulo

### 4.1 `src/thread_studio/schema.py`
- Normalização de parâmetros de rosca: `nominal_dia`, `pitch`, `thread_length`, `hand` (`right` ou `left`), `starts` (1, 2 ou 3 entradas).
- Padrões pré-configurados: `pco1881`, `mason_70`, `mason_86`, `iso_metric`, `fdm_trapezoid_45`.
- Folgas: `diametral_clearance` (`0.05` a `0.60 mm`), `axial_clearance`.
- Parâmetros de corpo: recartilhado (*knurling* com profundidade e densidade), espessura de parede, diâmetros de entrada e saída do adaptador de mangueira.

### 4.2 `src/thread_studio/thread_math.py`
- Geração das seções transversais 2D dos perfis de rosca (crista, flancos com ângulo de 60° ISO ou 45° FDM, raio de raiz).
- Transformação helicoidal analítica: $\theta \in [0, 2\pi N]$, $z(\theta) = \frac{p}{2\pi}\theta$.
- Aplicação do chanfro Higbee: atenuação da altura do dente por função suave de transição nas espiras extremas.
- Cálculo de folga real e detecção matemática de colisão de flanco entre rosca macho e fêmea.

### 4.3 `src/thread_studio/mesh_generator.py`
- Geração das malhas NumPy 2-manifold para:
  - Fuso rosqueado macho (sólido ou vazado) e porca/tampa com rosca interna.
  - Pote com textura externa (canelada ou recartilhada) e tampa combinada.
  - Adaptador cônico de transição contínua com espigões *barb*.
  - Kit de calibração rápida (`generate_thread_calibration_kit`).
- **Garantia 2-manifold estrita:** Todas as conexões entre a hélice de rosca e o corpo cilíndrico devem ser topologicamente fechadas ($V - E + F = 2$).

### 4.4 `src/thread_studio/studio_ui.py`
- WebGL2 a 60 FPS com shader de iluminação técnica e corte axial dinâmico (*clipping plane*).
- **Lupa 2D Sincronizada:** Painel 2D renderizando o perfil dos fios em corte, exibindo a linha de engajamento, folgas nominais em `mm` e aviso de travamento.
- Controles de rotação contínua (simulação de rosqueamento da tampa).

### 4.5 `src/thread_studio/plugin_main.py`
- Registro de permissão: `orca.request_permissions(threading=True)`.
- Capabilities: `ThreadStudioPageCapability` (Aba superior) e `ThreadStudioDockCapability` (Painel lateral).
- Auto-materialização do `icon.svg` no `storage()`.
- Injeção direta no Plater via `WM_COPYDATA` (Windows) e Cocoa (macOS), configurando camada adaptativa/fina para os fios de rosca e perímetro sólido (4–5 paredes).

### 4.6 `scripts/build_and_install.py`
- Empacotador AST PEP 723 single-file gerando `dist/orca_thread_generator.py` e `.whl`.
- Instalação local em `%APPDATA%\OrcaSlicer\orca_plugins\orca_thread_generator\`.

---

## 5. Roteiro de Verificação & Testes

Para homologar a implementação:

```powershell
# 1. Compilar o bundle e instalar localmente
& "C:\Program Files\OrcaSlicer\python\python.exe" -B d:\Projects\orca-thread-generator\scripts\build_and_install.py

# 2. Executar suíte completa de testes com parada em qualquer warning
& "C:\Program Files\OrcaSlicer\python\python.exe" -W error -m unittest discover -s d:\Projects\orca-thread-generator\tests -v
```

**Critérios de Aprovação:**
- [ ] 100% dos testes passam sem erros nem warnings (`-W error`).
- [ ] Todas as roscas geradas são perfeitamente estanques (zero arestas abertas).
- [ ] O chanfro Higbee suaviza perfeitamente a entrada e saída do filete.
- [ ] O bundle único `dist/orca_thread_generator.py` carrega standalone sem `src/`.
- [ ] O OrcaSlicer abre o plugin tanto na aba superior quanto no painel lateral.
