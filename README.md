# O que este commit resolve

Resumo: este commit adiciona uma configuração de workspace do VSCode que executa `git add "${file}"` automaticamente ao salvar arquivos Python, para que alterações apareçam no staging como esperado.

- Arquivo adicionado: [.vscode/settings.json](.vscode/settings.json)

Motivação:
- Facilitar o fluxo onde, ao salvar um arquivo no VSCode, ele vai automaticamente para o staging do Git.
- Evitar que edições fiquem esquecidas sem serem adicionadas ao índice.

Como funciona:
- A configuração usa a extensão **Run On Save** (publisher: `emeraldwalk`) para executar o comando `git add` no arquivo salvo.

Passos para usar/testar:
1. Instale a extensão no VSCode:

```bash
code --install-extension emeraldwalk.runonsave
```

2. Recarregue o VSCode (Command Palette → Reload Window) ou reinicie.
3. Abra um arquivo `.py`, altere e salve. O comando `git add <arquivo>` será executado automaticamente.
4. Verifique com:

```bash
git status --porcelain
```

Notas importantes:
- Arquivos listados em `.gitignore` não serão adicionados a menos que você force (`git add -f`). Ex.: arquivos em `__pycache__/` e `*.pyc` normalmente são ignorados.
- Se um arquivo foi marcado como `assume-unchanged` ou `skip-worktree`, use `git update-index --no-assume-unchanged <arquivo>` ou `git update-index --no-skip-worktree <arquivo>` para que mudanças voltem a ser detectadas.
- Use esta automação com cuidado em arquivos sensíveis — o comando é executado localmente no seu workspace.

Como reverter / remover:
- Remova ou edite [.vscode/settings.json](.vscode/settings.json) ou desative a extensão `emeraldwalk.runonsave`.

Próximo passo recomendado:
- Testar salvando um arquivo Python e confirmar que ele aparece em staging. Se preferir, posso executar esse teste localmente no repositório para você.
