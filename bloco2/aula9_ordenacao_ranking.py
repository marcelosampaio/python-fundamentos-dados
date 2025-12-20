import pandas as pd
from dados import obter_dados_exemplo

# ===============================
# Carregamento dos dados
# ===============================
df = obter_dados_exemplo()

# ===============================
# Coluna derivada: faturamento
# ===============================
df["faturamento"] = df["quantidade"] * df["valor_unitario"]

print("\n=== DataFrame original ===")
print(df)

# ===============================
# Ordenação por faturamento
# ===============================
print("\n=== Produtos ordenados por faturamento (desc) ===")
df_ordenado = df.sort_values("faturamento", ascending=False)
print(df_ordenado)

# ===============================
# Top 3 produtos por faturamento
# ===============================
print("\n=== Top 3 produtos por faturamento ===")
top_3 = df_ordenado.head(3)
print(top_3)

# ===============================
# Faturamento total por categoria (ordenado)
# ===============================
print("\n=== Faturamento total por categoria ===")
faturamento_categoria = (
    df.groupby("categoria")["faturamento"]
      .sum()
      .sort_values(ascending=False)
)
print(faturamento_categoria)

# ===============================
# Ranking explícito por faturamento
# ===============================
df["ranking_faturamento"] = df["faturamento"].rank(ascending=False)

print("\n=== Ranking explícito por faturamento ===")
print(df[["produto", "faturamento", "ranking_faturamento"]])

# ===============================
# Ranking explícito por quantidade
# ===============================
df["ranking_quantidade"] = df["quantidade"].rank(ascending=False)

print("\n=== Ranking explícito por quantidade vendida ===")
print(df[["produto", "quantidade", "ranking_quantidade"]])
