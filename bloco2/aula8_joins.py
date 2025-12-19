import pandas as pd
from dados import obter_dados_exemplo

# ===============================
# Criação do DataFrame principal
# ===============================
df_vendas = obter_dados_exemplo()

# Criando coluna derivada
df_vendas["faturamento"] = df_vendas["quantidade"] * df_vendas["valor_unitario"]

print("=== DataFrame de Vendas ===")
print(df_vendas)


# ===============================
# DataFrame de categorias
# ===============================
df_categorias = pd.DataFrame({
    "categoria": ["Eletrônicos", "Periféricos"],
    "descricao": ["Produtos eletrônicos", "Acessórios e periféricos"]
})

print("\n=== DataFrame de Categorias ===")
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


# ===============================
# RIGHT JOIN
# ===============================
right = pd.merge(df_vendas, df_categorias, on="categoria", how="right")
print("\n=== RIGHT JOIN ===")
print(right)


# ===============================
# OUTER JOIN
# ===============================
outer = pd.merge(df_vendas, df_categorias, on="categoria", how="outer")
print("\n=== OUTER JOIN ===")
print(outer)


# ===============================
# Comparação didática
# ===============================
print("\n=== Comparação de Resultados ===")
print(f"INNER: {len(inner)} linhas")
print(f"LEFT:  {len(left)} linhas")
print(f"RIGHT: {len(right)} linhas")
print(f"OUTER: {len(outer)} linhas")
