# Retail Data Analysis (Análise Exploratória de Dados de Varejo)

Este projeto apresenta um pipeline de Análise Exploratória de Dados (AED) aplicado ao setor varejista, utilizando Python para automatizar a limpeza, o tratamento de nulos, a validação de regras de negócio e a geração de visualizações gráficas.

## Objetivo

Praticar manipulação e saneamento de dados com Pandas, construindo um pipeline de ETL robusto e respondendo a perguntas operenciais e demográficas de negócio.

## Dados

O projeto utiliza uma base de dados transacionais de varejo armazenada na pasta `Base de Dados/`. 
A base contém informações como datas de compra, identificadores de transação, categorias de produtos, dados demográficos e gênero dos clientes. O script gera automaticamente uma versão limpa (`base_varejo_limpa.csv`).

## Perguntas Respondidas / Análises Realizadas

* Como tratar valores nulos e anomalias de sistema (como `#N/D`) preservando o volume de dados?
* Qual é a granularidade real da chave de transação (`CO_ID`)?
* Qual é o perfil estatístico da demografia de clientes (número de filhos, `CL_FHL`)?
* Quais são as top 10 categorias de produtos mais comercializadas?
* Como o volume de vendas evolui ao longo do tempo (sazonalidade)?
* Como as vendas se distribuem entre os gêneros dos clientes?

## Estrutura do Projeto

## Estrutura do Projeto

```text
Miniprojeto_LeonardoBorgesAlves_Analise_de_Dados_T6/
├── Base de Dados/
│   ├── base-varejo.csv
│   └── base_varejo_limpa.csv
├── código do desafio/
│   └── data_Code.py
├── graficos-varejo/
│   ├── grafico_top_categorias.png
│   ├── grafico_distribuicao_filhos.png
│   ├── grafico_evolucao_vendas.png
│   └── grafico_genero_clientes.png
├── Documentação/
└── README_LeonardoBorgesAlves_Analise_de_Dados_T6.md
````
    
## Status

Concluído.
