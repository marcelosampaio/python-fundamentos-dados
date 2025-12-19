from dados import obter_dados_exemplo

df = obter_dados_exemplo()

print("=== Operações em colunas ===")

print(f"Total de itens vendidos: {df['quantidade'].sum()}")
print(f"Preço médio unitário: R${df['valor_unitario'].mean():.2f}")
print(f"Quantidade de vendas: {df['produto'].count()}")
print(f"Menor preço: R${df['valor_unitario'].min():.2f}")
print(f"Maior preço: R${df['valor_unitario'].max():.2f}")
