import pandas as pd
import requests

URL = "https://brasilapi.com.br/api/feriados/v1/2026"


def carregar_feriados(url: str) -> pd.DataFrame:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    dados = response.json()
    df = pd.DataFrame(dados)
    print(df.head(10))
    return df


if __name__ == "__main__":
    carregar_feriados(URL)
