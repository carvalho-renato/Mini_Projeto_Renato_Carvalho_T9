"""Etapa 5: padrões de agrupamento com groupby() e pivot_table()."""

import pandas as pd

from carrega_dados import carregar_dados
from limpeza_dados import limpar_dados


def agrupar_por(df, coluna):
    """Agrupa por uma dimensão e calcula indicadores de volume."""
    resultado = (
        df.groupby(coluna)
        .agg(
            compras=("CO_ID", "nunique"),
            clientes=("CL_ID", "nunique"),
            itens=("PR_ID", "size"),
        )
        .sort_values("itens", ascending=False)
        .reset_index()
    )
    resultado["participacao_%"] = (
        resultado["itens"] / resultado["itens"].sum() * 100
    ).round(2)
    return resultado


def tabela_dinamica(df):
    """Combinação cruzada: categoria do produto x gênero do cliente."""
    return pd.crosstab(
        index=df["PR_CAT"],
        columns=df["CL_GENERO"],
        margins=True,
        margins_name="TOTAL",
    ).reset_index()



def evolucao_mensal(df):
    """Variação das compras ao longo do tempo."""
    df = df.copy()
    df["ANO_MES"] = df["DATA"].dt.strftime("%Y-%m")
    return (
        df.groupby("ANO_MES")
        .agg(compras=("CO_ID", "nunique"), clientes=("CL_ID", "nunique"))
        .reset_index()
        .sort_values("ANO_MES")
    )


def executar_agrupamentos(df):
    """Executa os agrupamentos obrigatórios (no mínimo dois)."""
    print("AGRUPAMENTO 1 - Compras por gênero do cliente")
    print(agrupar_por(df, "CL_GENERO").to_string(index=False))

    print("\nAGRUPAMENTO 2 - Categorias mais compradas")
    print(agrupar_por(df, "PR_CAT").head(10).to_string(index=False))

    print("\nAGRUPAMENTO 3 - Compras por segmento do cliente")
    print(agrupar_por(df, "CL_SEG").to_string(index=False))

    print("\nAGRUPAMENTO 4 - Evolução mensal das compras")
    print(evolucao_mensal(df).to_string(index=False))

    print("\nAGRUPAMENTO 5 - Tabela dinâmica: categoria x gênero")
    print(tabela_dinamica(df).to_string(index=False))


if __name__ == "__main__":
    df = limpar_dados(carregar_dados())
    executar_agrupamentos(df)