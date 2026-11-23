# Idiomas modulares / Modular languages

Thread Studio oferece Português, English, Español, Italiano, Français, Deutsch e 日本語, na aba e no painel lateral. O seletor segue o padrão do Box Studio. A escolha manual é salva nos dados locais do plugin, compartilhada entre aba e painel, e preservada ao sincronizar a impressora, restaurar valores ou desfazer/refazer alterações.

Trocar de idioma não gera uma malha nova. Parâmetros numéricos, nomes digitados pelo usuário, nomes de presets pessoais, caminhos de exportação e a geometria mantêm seus valores. Os avisos conhecidos, as opções, os modelos internos, as legendas e os textos de exportação acompanham o idioma selecionado. Detalhes técnicos desconhecidos retornados pelo sistema operacional permanecem no idioma de origem.

## Adicionar um idioma

1. Crie um JSON em `src/thread_studio/locales/`, usando `en.json` como referência. Exemplo parcial:

```json
{
  "schema_version": 1,
  "code": "nl",
  "native_name": "Nederlands",
  "direction": "ltr",
  "order": 7,
  "translations": {
    "Model Gallery": "Modellengalerij",
    "Save": "Opslaan"
  }
}
```

2. Execute `python -B -W error scripts/build_and_install.py --no-install` e os testes.
3. Distribua os instaladores verificados e reinicie o OrcaSlicer depois da instalação. O novo idioma aparecerá no seletor sem alterações em listas Python ou JavaScript.

O código regional `nl_NL.UTF-8` procura primeiro `nl-nl` e depois `nl`. Uma tradução ausente usa o texto inglês. Os JSONs são dados: não podem conter HTML ou código; marcadores como `{height}` precisam ser preservados. O build rejeita catálogos inválidos e chaves duplicadas. Um arquivo opcional inválido é ignorado em execução sem impedir a abertura do plugin.

O wheel inclui os JSONs legíveis. Os arquivos `.py` e `_any.py` incluem os catálogos compactados e funcionam sozinhos, offline, sem dependência adicional. Um JSON em `locales/` ao lado de um bundle também pode acrescentar um idioma ao iniciar o processo. Para incluí-lo em futuras instalações, mantenha o JSON no repositório e gere novamente os três artefatos.

O formato é o mesmo de Gear, Vase e Box; cada plugin tem sua cópia independente do carregador. Nenhum importa o projeto irmão. Código reutilizado mantém a licença MIT do repositório.

## Verification

Tests check complete catalog coverage for production labels, options, built-in presets and accessibility text. A synthetic Dutch catalog is added only to a temporary project, then rebuilt and imported from source, standalone, universal bundle and wheel. Browser checks exercise page/dock discovery and English fallback. Invalid optional packs, placeholder mismatches, duplicates and strict build failures are covered.

Controller tests verify persistence across a new controller, page/dock broadcasts, a language change while geometry is pending, reset/undo/redo behavior and identical vertices/triangles across languages. Browser acceptance checks cover seven languages, both themes and layouts, live Mason 86 warnings, user-entered names, printer synchronization, reload and real isolated STL/3MF exports. Native transport is disabled in browser checks; they never print or import into an installed OrcaSlicer.
