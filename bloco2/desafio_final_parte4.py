import pandas as pd
from dados import obter_dados_exemplo

# data frame com todos os dados de exemplo
df = obter_dados_exemplo()

# filtrar os produtos da categoria periféticos
filtro_perifericos = df["categoria"] == "Periféricos"
df_perifericos = df[filtro_perifericos]
print("=== Produtos da categoria periféricos ===")
print(df_perifericos)

# filtrar produtos com quantidade maior ou igual a 3
filtro_quantidade_maior_igual_3 = df["quantidade"] >= 3
df_quantidade_maior_igual_3 = df[filtro_quantidade_maior_igual_3]
print("\n=== Produtos com quantidade maior ou igual a 3 ===")
print(df_quantidade_maior_igual_3)

# filtro combinado  - categoria periféricos e quantidade maior ou igual a 3
filtro_combinado = filtro_perifericos & filtro_quantidade_maior_igual_3
df_filtro_combinado = df[filtro_combinado]
print("\n=== Produtos da categoria periféricos e quantidade maior ou igual a 3 ===")
print(df_filtro_combinado)

