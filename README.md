# python-fundamentos-dados

Repositório com exercícios básicos de Python e pandas.

## Conteúdo principal

* `requirements.txt` — dependência principal: `pandas`.
* `bloco2/dados.py` — `obter_dados_exemplo()` retorna um `DataFrame` de vendas (produto, categoria, quantidade, valor_unitario).
* `bloco2/aula3_dataframe_series.py` — imprime o `DataFrame` e colunas individuais.
* `bloco2/aula4_operacoes_colunas.py` — imprime métricas agregadas (soma, média, contagem, mínimo, máximo).
* `bloco2/aula5_colunas_calculadas.py` — cria coluna calculada `faturamento` (quantidade * valor_unitario) e imprime o faturamento total.
* `bloco2/aula6_filtragem_dados.py` — demonstra filtragem de dados em um `DataFrame` usando condições lógicas (similar a `WHERE` em SQL).
* `bloco2/aula7_groupby.py` — demonstra agrupamento com `groupby()` e agregações (`sum()`, `mean()`) para resumos por categoria.
* `bloco2/aula8_joins.py` — demonstra operações de `merge` (`INNER`, `LEFT`, `RIGHT`, `OUTER`) entre DataFrames para unir informações complementares.
* `bloco2/aula9_ordenacao_ranking.py` — demonstra ordenação de dados, identificação de **Top N** e criação de **rankings** usando `sort_values()`, `head()` e `rank()`.

## Execução rápida

```bash
python3 -m pip install -r requirements.txt
python3 bloco2/aula3_dataframe_series.py
python3 bloco2/aula4_operacoes_colunas.py
python3 bloco2/aula5_colunas_calculadas.py
python3 bloco2/aula6_filtragem_dados.py
python3 bloco2/aula7_groupby.py
python3 bloco2/aula8_joins.py
python3 bloco2/aula9_ordenacao_ranking.py
```

## Resumos das aulas recentes

### Aula 6 — Filtragem de Dados

Aprendemos a selecionar subconjuntos de um `DataFrame` usando condições lógicas (máscaras booleanas), equivalente ao `WHERE` do SQL. Foram utilizados operadores relacionais, combinações com `&` e `|`, e seleção explícita com `.loc`.

### Aula 7 — Agrupamento com `groupby`

Realizamos agrupamentos por chave (ex.: `categoria`) e aplicamos funções de agregação como `sum()` e `mean()` para obter resumos consolidados, permitindo análises comparativas entre grupos.

### Aula 8 — Joins / Merge

Demonstramos como unir DataFrames com `pd.merge()` utilizando diferentes tipos de junção (`inner`, `left`, `right`, `outer`), simulando operações de JOIN do SQL para combinar informações relacionadas.

### Aula 9 — Ordenação, Ranking e Top N

Exploramos a ordenação de dados com `sort_values()`, a seleção dos registros mais relevantes com `head()` (Top N) e a criação de rankings explícitos com `rank()`. Esses conceitos foram aplicados tanto aos dados originais quanto a resultados de agregações, reforçando práticas comuns em análises exploratórias e relatórios.

## Notas

* Diretórios `__pycache__/`, arquivos `*.py[cod]` e ambientes virtuais estão listados no `.gitignore` e não são versionados.
