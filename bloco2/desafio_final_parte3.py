import pandas as pd
from dados import obter_dados_exemplo

# data frame com todos os dados de exemplo
df = obter_dados_exemplo()

# Crie uma nova coluna chamada faturamento
df["faturamento"] = df["quantidade"] * df["valor_unitario"]
print("=== DataFrame com a nova coluna faturamento ===")
print(df)

# calculo do faturamento total
faturamento_total = df["faturamento"].sum()
print("\n=== Faturamento total ===")
print(faturamento_total)

# faturamento médio por venda
faturamento_medio = df["faturamento"].mean()
print("\n=== Faturamento médio por venda ===")
print(faturamento_medio)

