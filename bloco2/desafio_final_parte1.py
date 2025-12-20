import pandas as pd
from dados import obter_dados_exemplo

# data frame com todos os dados de exemplo
df = obter_dados_exemplo()

# exibir os 5 primeiros registros
print("=== 5 primeiros registros ===")
print(df.head())


# exibir os tipos de dados de cada coluna
print("\n=== Tipos de dados das colunas ===")
print(df.dtypes)


# exibir a coluna produto
print("\n=== Coluna produto ===")
print(df["produto"])

# exibir a coluna quantidade
print("\n=== Coluna quantidade ===")
print(df["quantidade"])

