
# Descrição do que este commit adiciona

Resumo: este commit adicionou um arquivo de configuração de workspace do VSCode e um README explicativo.

Arquivos alterados/adicione:
- `.vscode/settings.json` — contém uma configuração que, se seu editor estiver configurado para executar comandos ao salvar (por exemplo, usando uma extensão que rode comandos on-save), executa `git add "${file}"` ao salvar arquivos `.py`.
- `README.md` — este arquivo, que documenta o que foi feito e como testar.

Observação importante sobre o editor:
- O repositório contém um exemplo de configuração que utiliza a chave `emeraldwalk.runonsave` no arquivo de settings. Se você não utiliza essa extensão ou outra que rode comandos ao salvar, essa configuração não terá efeito. Mantenha ou remova o arquivo `.vscode/settings.json` conforme sua preferência.

# O que o projeto faz até agora

Este repositório é um conjunto de exercícios de fundamentos de Python focados em manipulação de dados com `pandas`.

Conteúdo atual relevante:
- `requirements.txt` — lista a dependência `pandas`.
- `bloco2/dados.py` — função `obter_dados_exemplo()` que retorna um `DataFrame` de exemplo com registros de vendas (produto, categoria, quantidade, valor_unitario).
- `bloco2/aula3_dataframe_series.py` — script que importa `obter_dados_exemplo()`, imprime o `DataFrame` completo e mostra impressão separada de algumas colunas (`produto`, `categoria`, `quantidade`, `valor_unitario`).

Como rodar o exemplo localmente:

```bash
python3 -m pip install -r requirements.txt
python3 bloco2/aula3_dataframe_series.py
```

# Como testar a automação de staging (opcional)

Se quiser que arquivos sejam automaticamente adicionados ao staging ao salvar, configure seu editor para executar o comando abaixo ao salvar (ou use uma extensão equivalente):

```bash
git add "${file}"
```

Depois de salvar um arquivo modificado, verifique o staging com:

```bash
git status --porcelain
```

Notas adicionais:
- Arquivos listados em `.gitignore` (ex.: `__pycache__/`, `*.pyc`) não serão adicionados automaticamente, a menos que você force com `git add -f`.
- Se um arquivo estiver marcado com `assume-unchanged` ou `skip-worktree`, atualize o índice com `git update-index --no-assume-unchanged <arquivo>` ou `git update-index --no-skip-worktree <arquivo>` para voltar a rastrear alterações.

Se quiser, adapto a configuração em `.vscode/settings.json` para o comportamento exato do seu editor (me diga qual extensão ou mecanismo você usa para executar comandos ao salvar). 
