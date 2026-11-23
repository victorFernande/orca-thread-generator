# Manual — Orca Thread Studio

## Instalação e interface

Após instalar ou atualizar, feche e reabra o OrcaSlicer. Confira a versão e ative **Orca Thread Studio** no gerenciador de plugins.

O template segue o Orca Vase Studio: nome e impressora no cabeçalho, ações compactas, galeria de cartões com filtros, parâmetros com sliders e campos numéricos, cartões de recursos e rodapé fixo de exportação. Clique na identificação da impressora para sincronizar seus dados. Trocar o material visual não seleciona um filamento de impressão.

## Primeiro projeto

1. Abra a aba **Thread Studio**, ou o script **Orca Thread Studio — Painel Lateral**.
2. Escolha um dos 12 projetos da biblioteca. Os presets são pontos de partida editáveis.
3. Ajuste diâmetro nominal, passo axial, comprimento e número de entradas. O avanço por volta é passo × entradas; mudar o número de entradas não muda o passo axial.
4. Defina a folga diametral e axial. A lupa informa a metade da folga diametral como folga radial.
5. Selecione **3 anéis de calibração**, exporte ou envie para a mesa e imprima uma amostra. Os entalhes 1, 2 e 3 identificam folgas diametrais de 0,10, 0,18 e 0,26 mm. Os três anéis fêmea devem ser testados no macho correspondente; não formam um ensaio universal.
6. Volte ao conjunto, aplique a folga que funcionou e gere a peça final.

## Famílias de peças

**Pote + tampa:** diâmetro do corpo, altura, parede e fundo controlam o recipiente. A parte externa superior contém a rosca macho; a tampa imprime com a abertura para cima. A vedação opcional é um canal anular no fundo interno da tampa para receber uma junta, sem garantia de estanqueidade. A interface permite ajustar largura, profundidade e recuo.

**Tampa / gargalo:** escolha entre tampa fechada e gargalo aberto. PCO-1881 e Mason 70 têm avisos experimentais. Para Mason 86 informe os quatro valores medidos e marque a confirmação; sem isso a geração e a exportação ficam bloqueadas. Não use peças experimentais como tampa de recipiente pressurizado ou como peça alimentar.

**Adaptador:** diâmetros de entrada/saída, comprimento total e extensão das pontas definem a transição. Cada ponta pode ser lisa cônica, espigão, rosca macho ou fêmea. Para pontas lisas/espigão, o diâmetro designa a passagem interna; para roscas, designa o diâmetro nominal do filete. A prévia e a exportação rejeitam paredes que eliminariam a passagem útil.

**Parafuso + porca:** selecione cabeça sextavada, recartilhada ou borboleta. Furo zero gera parafuso sólido; um valor positivo gera passagem axial. A porca é aberta. Perfis métricos são aproximações ideais para impressão, sem classe de tolerância normalizada.

## Prévia e comandos

Arraste a prévia para orbitar e use a roda para aproximar. **Enquadrar** restaura a câmera. **Corte axial** revela a parede e os filetes. **Abertura** controla a separação da tampa; **Rosquear** anima rotação com translação compatível com o avanço da rosca. A lupa acompanha o deslocamento e indica interferência analítica ou ausência de engate; ela não simula deformação do plástico.

O modo lateral usa as abas **Forma, Recursos, Impressão e Presets**, com prévia compacta no topo e exportação acessível no rodapé. O estado e os presets são compartilhados com a aba principal enquanto o plugin está carregado. Desfazer/refazer funciona entre as duas superfícies, e **Restaurar** retorna aos parâmetros iniciais. O botão PT/EN troca o idioma e o botão de tema alterna claro/escuro. **Surpreenda-me** gera uma configuração validada da família atual; ele não confirma medidas experimentais nem libera Mason 86 automaticamente.

## Exportação

Escolha conjunto, peça principal, secundária ou calibrador. STL exporta uma malha por peça; 3MF mantém múltiplos objetos e configurações mecânicas. Objetos são distribuídos na mesa sem redução de escala. Uma mesa insuficiente gera erro; exporte partes separadas ou selecione uma impressora maior.

**Enviar para a mesa** prepara o arquivo e aguarda a resposta do transporte nativo. “Pedido enviado” significa que a solicitação foi transmitida; confirme a presença das peças no OrcaSlicer. Em falha de integração, use **Abrir pasta de exportações** e importe o arquivo manualmente. Os arquivos e presets permanecem no armazenamento local do plugin.

As estimativas de minutos do planejamento original dependem do perfil real de fatiamento e não são prazos garantidos. Calibre contra a peça física antes de confiar no encaixe.
