# python-fundamentos-dados

Repositório com exercícios básicos de Python e pandas.

Conteúdo principal:
- `requirements.txt` — `pandas`.
- `bloco2/dados.py` — `obter_dados_exemplo()` retorna um `DataFrame` de vendas (produto, categoria, quantidade, valor_unitario).
- `bloco2/aula3_dataframe_series.py` — imprime o `DataFrame` e colunas individuais.
- `bloco2/aula4_operacoes_colunas.py` — imprime métricas agregadas (soma, média, contagem, mínimo, máximo).
 - `bloco2/aula5_colunas_calculadas.py` — cria coluna calculada `faturamento` (quantidade * valor_unitario) e imprime o faturamento total.

Execução rápida:

```bash
python3 -m pip install -r requirements.txt
python3 bloco2/aula3_dataframe_series.py
python3 bloco2/aula4_operacoes_colunas.py
python3 bloco2/aula5_colunas_calculadas.py
```

Notas:
- Arquivos em `__pycache__/`, `*.py[cod]`, e diretórios de ambientes virtuais estão listados em `.gitignore` e não são versionados por padrão.
