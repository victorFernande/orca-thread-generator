# Studio interface template / Template da interface

## Português

O Orca Vase Studio é a referência visual escolhida para a interface 1.1 do Thread. A base é o template MIT em `src/vase_studio/studio_ui.py`, revisão `a120c70d946a45136b0076a529ff806296b491c4`, do projeto de referência. As medidas, fontes, tokens claros/escuros e componentes são copiados; o conteúdo e as ferramentas correspondem a roscas, recipientes, adaptadores e fixadores.

O plugin mantém sua própria cópia do template, incorporada ao bundle e ao wheel, sem depender da instalação dos outros geradores. A prévia continua recebendo as malhas Python do Thread. A lupa permanece específica das roscas e acompanha a posição de engate; não é um simulador de esforço ou deformação.

A aba principal usa galeria e dimensões à esquerda, prévia e lupa ao centro e recursos de encaixe/impressão à direita. O rodapé de exportação permanece acessível. O painel lateral usa uma prévia compacta e as seções Forma, Recursos, Impressão e Presets.

Trocar o material visual não troca o filamento no OrcaSlicer. Ações de geração aleatória não confirmam medidas experimentais. Mason 86 continua exigindo medidas reais e confirmação explícita. O registro de verificações está em [VALIDATION.md](VALIDATION.md).

## English

Orca Vase Studio is the visual reference selected for the Thread 1.1 interface. Its MIT template at `src/vase_studio/studio_ui.py`, revision `a120c70d946a45136b0076a529ff806296b491c4`, supplies the dimensions, typography, light/dark tokens and components. Content and tools describe threads, containers, adapters and fasteners.

An independent copy is embedded in this plugin's bundle and wheel. Preview surfaces still come from the Thread Python geometry engine; the engagement loupe follows screw position. Visual material selection does not change filament. Random generation never confirms experimental measurements, and Mason 86 retains its explicit measurement gate. See [VALIDATION.md](VALIDATION.md) for recorded checks.

## Reproducing browser checks / Reproduzir testes no navegador

Browser tooling is a development dependency only. With Python 3.12+, NumPy and Node.js installed:

```console
npm install --no-save --package-lock=false playwright@1.62.1
npx playwright install chromium
node scripts/check_ui_template.cjs
```

`ORCA_TEST_PYTHON` selects the Python executable; `ORCA_UI_OUTPUT` selects the evidence directory. The runner starts a private localhost backend using temporary storage, blocks native delivery and folder opening, compares the generated interface with frozen Vase measurements, and checks real Python mesh updates and 3MF exports. It writes screenshots and a JSON report outside tracked source by default. This is not a test inside OrcaSlicer.

A suíte Python continua disponível com `python -B -W error -m unittest discover -s tests -v`. No CI, os testes Python rodam nos três sistemas e o navegador isolado roda no Linux. O aplicativo final não utiliza Node.js nem Playwright.
