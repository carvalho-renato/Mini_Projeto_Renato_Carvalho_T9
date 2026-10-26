"""Etapa 2 e 3: Limpeza, tratamento de texto, números, condicionais e datas."""

import re

import pandas as pd

from carrega_dados import carregar_dados


def limpar_texto_regex(texto):
    """Remove caracteres especiais desnecessários e espaços extras usando Expressões Regulares (re)."""
    if pd.isna(texto):
        return texto
    # Mantém apenas letras, números e espaços simples
    texto_limpo = re.sub(r"[^\w\s]", "", str(texto))
    # Substitui múltiplos espaços por um único espaço
    texto_limpo = re.sub(r"\s+", " ", texto_limpo).strip()
    return texto_limpo


def atribuir_categoria(cat):
    """Regra de Negócio com if/else:

    Preenche categorias vazias com 'Sem Categoria'.
    """
    if pd.isna(cat) or str(cat).strip() == "" or str(cat).lower() == "nan":
        return "Sem Categoria"
    return str(cat).strip().title()


def limpar_dados(df):
    # Cria uma cópia para preservar o dataframe original
    df = df.copy()

    # 1. Tratamento de Categorias vazias (Critério 4 - if/else)
    df["PR_CAT"] = df["PR_CAT"].apply(atribuir_categoria)

    # 2. Limpeza de Textos com regex e métodos de string
    colunas_texto = ["PR_NOME", "CL_GENERO", "CL_SEG"]
    for col in colunas_texto:
        if col in df.columns:
            df[col] = df[col].apply(limpar_texto_regex)

    # 3. Tratamento de Inteiros (Coluna de filhos: CL_FHL)
    # Converte para numérico, trata nulos com a mediana e converte para inteiro
    df["CL_FHL"] = pd.to_numeric(df["CL_FHL"], errors="coerce")
    mediana_filhos = df["CL_FHL"].median()
    df["CL_FHL"] = df["CL_FHL"].fillna(mediana_filhos).astype(int)

    # 4. Tratamento e Validação da Regra do Identificador de Compra (CO_ID)
    df = df[df["CO_ID"].notnull()]
    df = df[df["CO_ID"].astype(str).str.strip() != ""]

    # 5. Tratamento de Datas (Conversão para datetime com pd.to_datetime)
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
    # Remove registros com datas corrompidas, se houver
    df = df.dropna(subset=["DATA"])

    # 6. Remoção de Duplicatas
    df = df.drop_duplicates()

    return df


if __name__ == "__main__":
    df_bruto = carregar_dados()
    print("Linhas antes da limpeza:", len(df_bruto))

    df_tratado = limpar_dados(df_bruto)
    print("Linhas após a limpeza:", len(df_tratado))
    print("\nTipos de dados atualizados:")
    print(df_tratado.dtypes)
    print("\nValores nulos restantes:")
    print(df_tratado.isnull().sum())
    print("\nAmostra dos dados limpos:")
    print(df_tratado.head())

    # Salva a base tratada (arquivo de entrega obrigatório)
    df_tratado.to_csv("df_limpo.csv", sep=";", index=False, date_format="%d/%m/%Y")
    print("\nArquivo df_limpo.csv gerado.")