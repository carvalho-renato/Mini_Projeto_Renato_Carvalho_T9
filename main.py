"""Etapa 5 e 6: menu, relatório final no terminal e conclusões.

Executar com: python main.py
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from carrega_dados import carregar_dados
from limpeza_dados import limpar_dados

console = Console()

MENU = """
[bold cyan]1[/bold cyan] - Carregar a base bruta (Etapa 1)
[bold cyan]2[/bold cyan] - Limpar dados e gerar df_limpo.csv (Etapas 2 e 3)
[bold cyan]3[/bold cyan] - Estatística descritiva de CL_FHL (Etapa 4)
[bold cyan]4[/bold cyan] - Padrões de agrupamento (Etapa 5)
[bold cyan]5[/bold cyan] - Relatório final e conclusões
[bold cyan]0[/bold cyan] - Sair
"""


def relatorio_final(df):
    """Contadores do relatório final exibido no terminal."""
    console.rule("[bold blue]Relatório final - Base Varejo")

    compras = df["CO_ID"].nunique()
    clientes = df["CL_ID"].nunique()
    mulheres = df.loc[df["CL_GENERO"].str.upper() == "F", "CL_ID"].nunique()
    homens = df.loc[df["CL_GENERO"].str.upper() == "M", "CL_ID"].nunique()
    categoria_top = df["PR_CAT"].mode().iloc[0]
    produto_top = df.groupby(["PR_ID", "PR_NOME"]).size().idxmax()

    console.print(Panel(
        "\n".join([
            f"[bold]Período analisado ..:[/] {df['DATA'].min():%d/%m/%Y} a {df['DATA'].max():%d/%m/%Y}",
            f"[bold]Registros ..........:[/] {len(df):,}".replace(",", "."),
            f"[bold]Total de compras ...:[/] {compras:,}".replace(",", "."),
            f"[bold]Total de clientes ..:[/] {clientes:,}".replace(",", "."),
            f"[bold]Clientes mulheres ..:[/] {mulheres:,}".replace(",", "."),
            f"[bold]Clientes homens ....:[/] {homens:,}".replace(",", "."),
            f"[bold]Categoria destaque .:[/] {categoria_top}",
            f"[bold]Produto destaque ...:[/] SKU {produto_top[0]} - {produto_top[1]}",
            f"[bold]Média de filhos ....:[/] {df['CL_FHL'].mean():.3f}",
        ]),
        title="Resumo geral",
        expand=False,
    ))

    conclusoes = [
        "A base original tinha 830.000 registros; após a remoção de duplicatas "
        "restaram 733.447 registros únicos.",
        "Não havia nulos nas colunas reais, mas a rotina de limpeza trata nulos de "
        "forma completa, ficando robusta a mudanças na base.",
        f"A categoria {categoria_top} concentra o maior volume de itens vendidos.",
        "O público feminino responde pela maior parte das compras da base.",
        "As compras se distribuem de forma estável ao longo dos meses, sem "
        "sazonalidade marcada.",
        "Problema remanescente: uma linha duplicada pode ser o mesmo item comprado "
        "2x na mesma compra; usar Base_Varejo_original.csv caso as repetições sejam reais.",
    ]

    console.print(Panel(
        "\n".join(f"  {i}. {texto}" for i, texto in enumerate(conclusoes, 1)),
        title="Conclusões",
        expand=False,
    ))
    return conclusoes


def main():
    acoes = {
        "1": lambda: print(carregar_dados().head(10)),
        "2": lambda: print(f"Base limpa: {len(limpar_dados(carregar_dados()))} registros "
                           f"-> df_limpo.csv gerado"),
        "3": lambda: __import__("estatistica_dados"),
        "4": lambda: __import__("agrupamento_dados").executar_agrupamentos(
            limpar_dados(carregar_dados())),
        "5": lambda: relatorio_final(limpar_dados(carregar_dados())),
    }

    while True:
        console.print("\n[bold]Mini-projeto Análise de Dados - Base Varejo[/bold]")
        console.print(MENU)
        escolha = Prompt.ask("Escolha uma opção", default="0").strip()

        if escolha == "0":
            console.print("[bold]Encerrando...[/bold]")
            return

        acao = acoes.get(escolha)
        if acao is None:
            console.print("[bold red]Opção inválida.[/bold red]")
            continue

        try:
            acao()
        except FileNotFoundError as falha:
            console.print(f"[bold red]{falha}[/bold red]")
        except Exception as falha:  # noqa: BLE001
            console.print(f"[bold red]Falha ao executar a etapa: {falha}[/bold red]")


if __name__ == "__main__":
    main()