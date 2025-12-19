import pandas as pd

def obter_dados_exemplo():
    """Retorna um DataFrame de exemplo usado nas aulas."""
    data = {
        "nome": ["Ana", "Bruno", "Carla"],
        "idade": [23, 35, 29],
        "peso": [60.5, 82.3, 55.0],
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    print(obter_dados_exemplo())
