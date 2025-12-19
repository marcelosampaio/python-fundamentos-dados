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
- `bloco2/aula8_joins.py` — demonstra operações de `merge` (INNER, LEFT, RIGHT, OUTER) entre DataFrames para unir informações complementares.

Execução rápida:

```bash
python3 -m pip install -r requirements.txt
python3 bloco2/aula3_dataframe_series.py
python3 bloco2/aula4_operacoes_colunas.py
python3 bloco2/aula5_colunas_calculadas.py
python3 bloco2/aula6_filtragem_dados.py
python3 bloco2/aula7_groupby.py
python3 bloco2/aula8_joins.py
```

Resumos das aulas recentes:

- **Aula 6 — Filtragem de Dados**

	Aprendemos a selecionar subconjuntos de um `DataFrame` usando condições lógicas (máscaras booleanas), equivalente ao `WHERE` do SQL. Exemplos: filtrar por coluna, combinar condições com `&`/`|`, e aplicar `.loc` para seleção.

- **Aula 7 — Agrupamento com `groupby`**

	Agrupamos registros por uma chave (ex.: `categoria`) e aplicamos funções de agregação como `sum()` e `mean()` para obter resumos consolidados por grupo.

- **Aula 8 — Joins / Merge**

	Demonstramos como unir DataFrames com `pd.merge()` usando diferentes tipos de join (`inner`, `left`, `right`, `outer`) para combinar informações (ex.: juntar vendas com descrições de categoria).

Notas:
- Arquivos em `__pycache__/`, `*.py[cod]`, e diretórios de ambientes virtuais estão listados em `.gitignore` e não são versionados por padrão.
