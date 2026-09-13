# 📊 Análise Exploratória de Dados (AED) Aplicada ao Varejo

[![Status do Projeto](https://img.shields.io/badge/Status-Concluído-success.svg)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-blueviolet.svg)](https://seaborn.pydata.org/)

Repositório oficial desenvolvido para a submissão do **Mini-Projeto Avaliativo do Módulo 1 (Semana 07)** da turma de **Análise de Dados T6**. 

---

## 🎯 1. Contextualização e Objetivo
Este projeto consiste no desenvolvimento de uma **Análise Exploratória de Dados (AED)** aplicada ao setor varejista, automatizando a transformação de registros brutos de compras em informações acionáveis. O objetivo técnico é auditar a qualidade dos dados, realizar processos de limpeza estrutural e tipológica, extrair parâmetros estatísticos descritivos e responder a perguntas operacionais fundamentais para Business Intelligence (BI).

A base utilizada (`base-varejo.csv`) contém transações reais de compras, incluindo datas, identificadores de transação, dados demográficos dos clientes e categorias de produtos.

---

## 📚 2. Stack Tecnológica e Bibliotecas Utilizadas
Todo o código foi desenvolvido em **Python 3.x** utilizando um conjunto robusto de bibliotecas especializadas em ciência de dados e engenharia de software:

| Biblioteca | Versão / Uso Principal no Projeto | Justificativa Técnica |
| :--- | :--- | :--- |
| **`pandas`** | Manipulação de Dados (`pd.read_csv`, `DataFrame`, `groupby`) | Essencial para a leitura estruturada do arquivo CSV, tratamento de valores nulos, eliminação de duplicatas (`drop_duplicates`) e agregações complexas. |
| **`numpy`** | Computação Numérica e Vetorizada | Utilizada nos bastidores pelo pandas e para suporte a operações matemáticas de alta performance. |
| **`matplotlib.pyplot`** | Renderização de Gráficos (`plt.figure`, `plt.savefig`) | Biblioteca base de plotagem em Python, utilizada para estruturar a tela (canvas), definir eixos, títulos e salvar as imagens em alta resolução (`dpi=300`). |
| **`seaborn`** | Visualização Estatística (`sns.barplot`, `sns.countplot`, `sns.lineplot`) | Construída sobre o Matplotlib, aplica paletas estéticas profissionais (`mako`, `crest`) e formata automaticamente gráficos estatísticos complexos. |
| **`os`** | Gestão de Caminhos e Diretórios (`os.path`, `os.makedirs`) | Permite criar um script **100% autônomo e portátil**, capaz de localizar pastas e arquivos de forma dinâmica independente de onde o avaliador execute o projeto. |

---

## 💻 3. Guia Passo a Passo: Como Executar no VS Code

Se você vai abrir e rodar este projeto utilizando o **Visual Studio Code (VS Code)**, siga rigorosamente este guia passo a passo:

### Passo 1: Abrir a Pasta Raiz no VS Code
1. Abra o **VS Code**.
2. No menu superior, clique em **File** > **Open Folder...** (Abrir Pasta...).
3. Selecione a pasta principal do projeto: **`Defesa Mini Projeto`**. (Não abra apenas a subpasta de código; abra a pasta raiz para que o script enxergue tanto a base quanto o código).

### Passo 2: Instalar as Extensões Necessárias
1. No menu lateral esquerdo do VS Code, clique no ícone de **Extensions** (Extensões) ou aperte `Ctrl+Shift+X`.
2. Certifique-se de ter instalado a extensão oficial **Python** (desenvolvida pela Microsoft).

### Passo 3: Instalar as Bibliotecas no Terminal
O código depende de bibliotecas externas que não vêm instaladas por padrão no Python. 
1. No VS Code, abra o terminal integrado clicando em **Terminal** > **New Terminal** no menu superior (ou use o atalho `` Ctrl + ` ``).
2. Certifique-se de que o terminal está apontando para a raiz do projeto e execute o comando abaixo para instalar todas as dependências de uma única vez:
   ```bash
   pip install pandas numpy matplotlib seaborn