# Revisão de idiomas dos Studios — 2026-11-23

A revisão confere catálogos e controles, não apenas a presença de um botão de idioma. Para cada atualização, verificar a lista descoberta, rótulos, opções, avisos, modelos internos, textos de exportação, persistência e sincronização entre aba e sidebar. Verificar que trocar de idioma não modifica a peça ou dispara geração desnecessária.

| Plugin | Catálogos encontrados | Cobertura observada |
| --- | --- | --- |
| Gear | PT, EN, ES, IT, FR, DE, JA | Interface com pacotes modulares; parte do PT usa o fallback bilíngue existente. |
| Vase | PT, EN, ES, IT, FR, DE, JA | Interface com pacotes modulares. |
| Box | PT, EN, ES, IT, FR, DE, JA | Interface com pacotes modulares; algumas chaves contextuais usam a tradução da frase geral. |
| Thread | PT, EN, ES, IT, FR, DE, JA | Esta alteração completa interface, opções, presets e avisos conhecidos. Antes, somente PT/EN. |
| Surface | PT, EN, ES, IT, FR, DE, JA | Os pacotes atuais cobrem **apenas os avisos**. A interface restante ainda contém textos em português. Tradução integral continua pendente. |

O código do Surface estava em alteração separada durante esta revisão e não foi modificado. A presença de sete arquivos não constitui validação de tradução integral, revisão editorial nativa ou teste dentro do aplicativo para todos os idiomas.

## Checklist para próximas alterações

- Conferir todos os Studios quando houver mudança no padrão compartilhado de idioma.
- Manter os idiomas descobertos a partir dos JSONs, inclusive no schema, no host e nos instaladores.
- Usar cobertura automática de chaves para impedir que um novo controle fique sem tradução.
- Testar aba e sidebar, temas claro/escuro, avisos já visíveis e mensagens recebidas posteriormente.
- Preservar texto pessoal e números. Registrar separadamente a validação isolada, a CI e a verificação no Orca instalado.
