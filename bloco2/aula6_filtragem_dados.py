from dados import obter_dados_exemplo

df = obter_dados_exemplo()

df["faturamento"] = df["quantidade"] * df["valor_unitario"]

print("=== Todas as vendas ===")
print(df)

filtro_categoria = df["categoria"] == "Periféricos"
filtro_quantidade = df["quantidade"] >= 4

df_filtrado = df[filtro_categoria & filtro_quantidade]

print("\n=== Periféricos com quantidade >= 4 ===")
print(df_filtrado)
