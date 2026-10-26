"""Etapa 1: ler o arquivo CSV com os dados do varejo."""

import os

import pandas as pd

# Caminho relativo à pasta deste script (evita o FileNotFoundError no VS Code)
CAMINHO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Base_Varejo.csv")


def carregar_dados():
    # 1. Separador ponto e vírgula
    # 2. Identificadores como string para não perder zeros à esquerda
    df = pd.read_csv(
        CAMINHO_CSV,
        sep=";",
        dtype={"CO_ID": str, "CL_ID": str, "PR_ID": str},
        encoding="utf-8",  # se der erro de acentuação, mude para "latin1"
    )

    # 3. Descarta as colunas vazias extras do final (;;;;)
    df = df.dropna(how="all", axis=1)

    return df


if __name__ == "__main__":
    df = carregar_dados()
    print(df.head(10))