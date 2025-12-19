# python-fundamentos-dados

Repositório com exercícios básicos de Python e pandas.

Conteúdo principal:
- `requirements.txt` — `pandas`.
- `bloco2/dados.py` — `obter_dados_exemplo()` retorna um `DataFrame` de vendas (produto, categoria, quantidade, valor_unitario).
- `bloco2/aula3_dataframe_series.py` — imprime o `DataFrame` e colunas individuais.
- `bloco2/aula4_operacoes_colunas.py` — imprime métricas agregadas (soma, média, contagem, mínimo, máximo).
 - `bloco2/aula5_colunas_calculadas.py` — cria coluna calculada `faturamento` (quantidade * valor_unitario) e imprime o faturamento total.
 - `bloco2/aula6_filtragem_dados.py` — demonstra filtragem de dados em um `DataFrame` usando condições lógicas (similar a `WHERE` em SQL).
 - `bloco2/aula7_groupby.py` — demonstra agrupamento com `groupby()` e agregações (`sum()`, `mean()`) para resumos por categoria.

Execução rápida:

```bash
python3 -m pip install -r requirements.txt
python3 bloco2/aula3_dataframe_series.py
python3 bloco2/aula4_operacoes_colunas.py
python3 bloco2/aula5_colunas_calculadas.py
python3 bloco2/aula6_filtragem_dados.py
python3 bloco2/aula7_groupby.py

# Aula 6 — Filtragem de Dados

Abordagem: Filtragem de Dados com pandas

Nesta aula, aprendemos a selecionar subconjuntos de dados em um DataFrame utilizando condições lógicas, de forma semelhante à cláusula WHERE do SQL.

# Aula 7 — Agrupamento com groupby

Nesta aula aprendemos a agrupar dados com `groupby` no pandas para gerar resumos por categoria, aplicando funções de agregação como `sum()` e `mean()`. Entendemos como o `groupby` organiza os dados por chave e permite análises consolidadas de forma simples e eficiente.
```

Notas:
- Arquivos em `__pycache__/`, `*.py[cod]`, e diretórios de ambientes virtuais estão listados em `.gitignore` e não são versionados por padrão.
