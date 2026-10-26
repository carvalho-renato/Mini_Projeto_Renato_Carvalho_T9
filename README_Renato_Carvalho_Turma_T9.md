# Mini-Projeto Avaliativo — Análise de Dados com Python

**Aluno:** Renato Carvalho
**Turma:** T9
**Repositório:** Miniprojeto_Renato_Carvalho_Turma_T9
**Módulo:** M1S07 — Mini-Projeto Avaliativo
**Base de dados:** Varejo — https://www.kaggle.com/datasets/namespaiva/base-varejo/data

Este arquivo é o **diário de bordo do projeto**. Ele é atualizado a cada
sprint entregue, registrando o que foi implementado, os arquivos envolvidos e
o commit correspondente. O histórico de commits do Git mostra a evolução
incremental da solução.

---

## Objetivo

Construir um pipeline de ETL (Extract, Transform, Load) em Python sobre a base
de varejo, aplicando: importação estruturada, transformação de tipos com
expressões regulares, tratamento de nulos e duplicatas, estatística descritiva
e padrões de agrupamento, finalizando com um relatório no terminal.

---

## Como executar

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
py -m venv .venv          # Windows
source .venv/bin/activate       # Linux / macOS

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Baixar a base e salvar como Base_Varejo.csv na raiz do projeto
#    https://www.kaggle.com/datasets/namespaiva/base-varejo/data

# 4. Executar as etapas na ordem
python carrega_dados.py         # Etapa 1 - importação
python limpeza_dados.py         # Etapas 2 e 3 - gera df_limpo.csv
python estatistica_dados.py     # Etapa 4 - estatística descritiva
python agrupamento_dados.py     # Etapa 5 - agrupamentos
python main.py                  # menu + relatório final


**Diário de bordo**

---

Sprint 2 — Transformação de tipos
limpar_texto_regex(): remove caracteres especiais e espaços duplicados com re.sub.
atribuir_categoria(): regra com if/else que preenche categorias vazias com Sem Categoria.
CL_FHL convertida para inteiro com tratamento de nulos pela mediana.
DATA convertida para datetime com pd.to_datetime(format="%d/%m/%Y").

---

Sprint 3 — Limpeza de nulos e duplicatas
Validação da regra do identificador de compra (CO_ID): registros vazios separados.
Remoção de datas corrompidas e de linhas duplicadas.
Geração do arquivo df_limpo.csv com a base tratada.

---

Sprint 4 — Estatística descritiva
Medidas calculadas para CL_FHL: contagem, média, mediana, moda, desvio
padrão, variância, mínimo, máximo, amplitude, Q1, Q2, Q3 e coeficiente de variação.
Distribuição de frequência e média de filhos por cliente único.
Exportação para estatisticas_filhos.xlsx.

---

Sprint 5 — Agrupamentos e relatório
Agrupamentos com groupby() por gênero, categoria, segmento e mês.
pivot_table() cruzando categoria do produto com gênero do cliente.
Relatório final no terminal com contadores e bloco de conclusões.

---

Sprint 6 — Versionamento
Repositório público no GitHub com commits progressivos por sprint.
README com reflexão teórica sobre ETL e qualidade de dados.

---

**Reflexão teórica: ETL e qualidade de dados**
ETL (Extract, Transform, Load) é o processo de extrair dados de uma origem,
transformá-los em informação confiável e carregá-los em um destino. Neste
projeto: a extração usa pandas.read_csv; a transformação concentra a limpeza
de textos com regex, a conversão de tipos e o tratamento de nulos e duplicatas;
e o carregamento grava o df_limpo.csv.

Qualidade de dados é o grau em que a base é adequada ao uso pretendido.
Os problemas encontrados foram classificados em:

Completude: valores ausentes nas colunas.
Unicidade: 96.553 linhas duplicadas.
Validade: datas fora do padrão dd/mm/aaaa.
Consistência: colunas extras geradas pelos ; no fim das linhas.
Cada tratamento foi justificado: registros sem identificador ou data foram
removidos por não serem rastreáveis; CL_FHL foi preenchida com a mediana por
ser robusta a valores extremos; e categorias vazias receberam o rótulo
Sem Categoria para não descartar a linha nem inventar informação.

**Principais insights**
A base original tem 830.000 registros; após a remoção de duplicatas restaram
733.447 registros únicos.
Não havia nulos nas colunas reais, mas a rotina de limpeza trata nulos de
forma completa, ficando robusta a alterações na base.
A maior parte das compras é realizada por clientes do gênero feminino.
As categorias de produto apresentam volumes muito distintos entre si.
As compras se distribuem de forma relativamente estável ao longo do período.
Problema remanescente: remover duplicatas pode apagar o mesmo produto
comprado duas vezes na mesma compra. Se as repetições forem reais, usar
Base_Varejo_original.csv.
