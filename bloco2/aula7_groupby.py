from dados import obter_dados_exemplo

df = obter_dados_exemplo()
df["faturamento"] = df["quantidade"] * df["valor_unitario"]

print("=== DataFrame original ===")
print(df)

print("\n=== Faturamento por categoria ===")
print(df.groupby("categoria")["faturamento"].sum())

print("\n=== Relatório consolidado ===")
relatorio = (
    df
    .groupby("categoria")["faturamento"]
    .agg(["sum", "mean", "count"])
)

print(relatorio)
