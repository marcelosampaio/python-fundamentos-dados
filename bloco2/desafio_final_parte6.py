import pandas as pd
from dados import obter_dados_exemplo, obter_categorias

df_vendas = obter_dados_exemplo()
df_categorias = obter_categorias()  

print("=== Dados de Vendas ===")
print(df_vendas)
print("\n=== Dados de Categorias ===")
print(df_categorias)    

# ===============================
# INNER JOIN
# ===============================
inner = pd.merge(df_vendas, df_categorias, on="categoria", how="inner")
print("\n=== INNER JOIN ===")
print(inner)


# ===============================
# LEFT JOIN
# ===============================
left = pd.merge(df_vendas, df_categorias, on="categoria", how="left")
print("\n=== LEFT JOIN ===")
print(left)