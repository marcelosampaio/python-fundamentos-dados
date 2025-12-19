from dados import obter_dados_exemplo

df = obter_dados_exemplo()

print("=== DataFrame completo ===")
print(df)

print("\n=== Coluna: produto ===")
print(df["produto"])

print("\n=== Coluna: categoria ===")
print(df["categoria"])

print("\n=== Coluna: quantidade ===")
print(df["quantidade"])

print("\n=== Coluna: valor_unitario ===")
print(df["valor_unitario"])
