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

