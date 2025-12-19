import pandas as pd

def obter_dados_exemplo():
    vendas = [
        {"produto": "Notebook", "categoria": "Eletrônicos", "quantidade": 2, "valor_unitario": 3000.00},
        {"produto": "Mouse", "categoria": "Periféricos", "quantidade": 5, "valor_unitario": 45.00},
        {"produto": "Teclado", "categoria": "Periféricos", "quantidade": 3, "valor_unitario": 120.00},
        {"produto": "Monitor", "categoria": "Eletrônicos", "quantidade": 1, "valor_unitario": 800.00},
        {"produto": "Webcam", "categoria": "Periféricos", "quantidade": 4, "valor_unitario": 250.00}
    ]

    return pd.DataFrame(vendas)


if __name__ == "__main__":
    print(obter_dados_exemplo())
