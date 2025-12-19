from dados import obter_dados_exemplo

df = obter_dados_exemplo()

df["faturamento"] = df["quantidade"] * df["valor_unitario"]

print("=== Todas as vendas ===")
print(df)

print("\n=== Apenas Eletrônicos ===")
print(df[df["categoria"] == "Eletrônicos"])

print("\n=== Quantidade >= 3 ===")
print(df[df["quantidade"] >= 3])

print("\n=== Periféricos com quantidade >= 4 ===")

filtro_categoria = df["categoria"] == "Periféricos"
filtro_quantidade = df["quantidade"] >= 4

df_filtrado = df[filtro_categoria & filtro_quantidade]

print(df_filtrado)