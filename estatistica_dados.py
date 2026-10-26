"""Etapa 4: estatística descritiva da coluna CL_FHL (número de filhos)."""

import pandas as pd

from carrega_dados import carregar_dados
from limpeza_dados import limpar_dados


def estatisticas_filhos(df):
    """Calcula todas as medidas descritivas pedidas para a coluna CL_FHL."""
    serie = df["CL_FHL"].dropna()
    moda = serie.mode()

    return {
        "contagem": int(serie.count()),
        "media": serie.mean(),
        "mediana": serie.median(),
        "moda": float(moda.iloc[0]) if not moda.empty else 0.0,
        "desvio_padrao": serie.std(),
        "variancia": serie.var(),
        "minimo": serie.min(),
        "maximo": serie.max(),
        "amplitude": serie.max() - serie.min(),
        "q1_25%": serie.quantile(0.25),
        "q2_50%": serie.quantile(0.50),
        "q3_75%": serie.quantile(0.75),
        "coef_variacao_%": (serie.std() / serie.mean() * 100) if serie.mean() else 0.0,
    }


def distribuicao_filhos(df):
    """Distribuição de frequência da quantidade de filhos por cliente."""
    contagem = df["CL_FHL"].value_counts().sort_index()

    tabela = pd.DataFrame({
        "filhos": contagem.index,
        "frequencia": contagem.values,
    })
    tabela["percentual"] = (tabela["frequencia"] / tabela["frequencia"].sum() * 100).round(2)
    tabela["acumulado_%"] = tabela["percentual"].cumsum().round(2)
    return tabela


def media_filhos_por_cliente(df):
    """Média de filhos com UMA linha por cliente (o atributo é do cliente, não da compra)."""
    clientes = df.sort_values("DATA").drop_duplicates(subset="CL_ID", keep="last")
    return clientes["CL_FHL"]


def salvar_relatorio(medidas, frequencias, caminho="estatisticas_filhos.xlsx"):
    """Exporta o relatório para Excel (openpyxl)."""
    tabela_medidas = pd.DataFrame(
        {"medida": list(medidas.keys()), "valor": list(medidas.values())}
    )
    with pd.ExcelWriter(caminho, engine="openpyxl") as escritor:
        tabela_medidas.to_excel(escritor, sheet_name="medidas", index=False)
        frequencias.to_excel(escritor, sheet_name="distribuicao", index=False)
    print(f"Relatório exportado para {caminho}")


if __name__ == "__main__":
    df = limpar_dados(carregar_dados())

    medidas = estatisticas_filhos(df)
    print("ESTATÍSTICAS - NÚMERO DE FILHOS (CL_FHL)")
    for nome, valor in medidas.items():
        print(f"  {nome}: {valor}")

    print("\nDistribuição de frequência:")
    frequencias = distribuicao_filhos(df)
    print(frequencias.to_string(index=False))

    por_cliente = media_filhos_por_cliente(df)
    print(f"\nMédia de filhos por cliente único: {por_cliente.mean():.3f} "
          f"({por_cliente.count()} clientes)")

    salvar_relatorio(medidas, frequencias)