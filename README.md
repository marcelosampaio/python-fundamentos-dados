
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
# python-fundamentos-dados

Repositório com exercícios básicos de Python e pandas.

Conteúdo principal:
- `requirements.txt` — `pandas`.
- `bloco2/dados.py` — `obter_dados_exemplo()` retorna um `DataFrame` de vendas (produto, categoria, quantidade, valor_unitario).
- `bloco2/aula3_dataframe_series.py` — imprime o `DataFrame` e colunas individuais.
- `bloco2/aula4_operacoes_colunas.py` — imprime métricas agregadas (soma, média, contagem, mínimo, máximo).

Execução rápida:

```bash
python3 -m pip install -r requirements.txt
python3 bloco2/aula3_dataframe_series.py
python3 bloco2/aula4_operacoes_colunas.py
```

Notas:
- O arquivo `.vscode/settings.json` foi removido do repositório (era apenas um exemplo para executar `git add` ao salvar).
- Arquivos em `__pycache__/`, `*.py[cod]`, e diretórios de ambientes virtuais estão listados em `.gitignore` e não são versionados por padrão.

Se quiser que eu adicione uma configuração específica de editor para auto-staging, diga qual editor/extensão você usa e eu preparo o exemplo.
