from dados import obter_dados_exemplo

df = obter_dados_exemplo()

df["faturamento"] = df["quantidade"] * df["valor_unitario"]

print("")
print("=== Colunas Calculadas ===")
print(df)
print(f"\n📍 Faturamento total: R${df['faturamento'].sum():.2f}")
print("")
