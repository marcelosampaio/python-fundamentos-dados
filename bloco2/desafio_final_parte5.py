from dados import obter_dados_exemplo

df = obter_dados_exemplo()

# criar coluna calculada
df["faturamento"] = df["quantidade"] * df["valor_unitario"]

# faturamento total por categoria
faturamento_por_categoria = df.groupby("categoria")["faturamento"].sum()
print("=== Faturamento total por categoria ===")
print(faturamento_por_categoria)

# faturamento médio por categoria
faturamento_medio_por_categoria = df.groupby("categoria")["faturamento"].mean()
print("\n=== Faturamento médio por categoria ===")
print(faturamento_medio_por_categoria)

# quantidade de produtos distintos por categoria
quantidade_produtos_por_categoria = df.groupby("categoria")["produto"].nunique()
print("\n=== Quantidade de produtos por categoria ===")
print(quantidade_produtos_por_categoria)

# ordenar pelo faturamento total (decrescente)
faturamento_ordenado = faturamento_por_categoria.sort_values(ascending=False)
print("\n=== Faturamento total por categoria (ordenado) ===")
print(faturamento_ordenado)

# EQUIVALENTE EM SQL:
#
# SELECT
#   categoria,
#   SUM(quantidade * valor_unitario) AS faturamento_total,
#   AVG(quantidade * valor_unitario) AS faturamento_medio,
#   COUNT(DISTINCT produto) AS qtd_produtos
# FROM vendas
# GROUP BY categoria
# ORDER BY faturamento_total DESC;
