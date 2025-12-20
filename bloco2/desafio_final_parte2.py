import pandas as pd
from dados import obter_dados_exemplo

# data frame com todos os dados de exemplo
df = obter_dados_exemplo()

# quantidade total de itens vendidos
total_itens_vendidos = df["quantidade"].sum()
print("=== Quantidade total de itens vendidos ===")
print(total_itens_vendidos)

# valor médio dos produtos
valor_medio_produtos = df["valor_unitario"].mean()
print("\n=== Valor médio dos produtos ===")
print(valor_medio_produtos)

# maior e menor valor unitário
maior_valor_unitario = df["valor_unitario"].max()
menor_valor_unitario = df["valor_unitario"].min()
print("\n=== Maior valor unitário ===")
print(maior_valor_unitario)
print("\n=== Menor valor unitário ===")
print(menor_valor_unitario)

# exibir o total de linhas do dataset
total_linhas = df.shape[0]
print("\n=== Total de linhas do dataset ===")
print(total_linhas)