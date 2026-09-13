import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# ⚙️ CONFIGURAÇÕES DO USUÁRIO
# ==========================================
SALVAR_GRAFICOS = True                  # True para gerar/salvar imagens | False para desativar
NOME_PASTA_GRAFICOS = "graficos-varejo" # Pasta dos gráficos (será gerada na raiz do projeto)

# Configuração de estilo visual para os gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

def encontrar_caminhos():
    """Mapeia os diretórios de forma inteligente baseado na estrutura do projeto."""
    diretorio_script = os.path.dirname(os.path.abspath(__file__)) # Pasta 'código do desafio'
    diretorio_pai = os.path.dirname(diretorio_script)             # Pasta raiz ('Defesa Mini Projeto')
    
    # Localiza a pasta 'Base de Dados'
    pasta_base_dados = os.path.join(diretorio_pai, "Base de Dados")
    if not os.path.exists(pasta_base_dados):
        pasta_base_dados = os.path.join(diretorio_script, "Base de Dados")
        if not os.path.exists(pasta_base_dados):
            pasta_base_dados = os.path.join(diretorio_script, "data-base")
            
    # Procura pelo arquivo da base de varejo
    possiveis_arquivos = ["base-varejo.csv", "Base Varejo.csv", "base_varejo.csv", "Base_Varejo.csv", "base-varejo"]
    caminho_base = None
    
    for arq in possiveis_arquivos:
        candidato = os.path.join(pasta_base_dados, arq)
        if os.path.exists(candidato):
            caminho_base = candidato
            break
            
    return diretorio_script, diretorio_pai, pasta_base_dados, caminho_base

def executar_pipeline_completo():
    print("="*80)
    print("🚀 PIPELINE DE ANÁLISE EXPLORATÓRIA DE DADOS (VAREJO) - NÍVEL PROFISSIONAL")
    print("="*80)
    
    diretorio_script, diretorio_pai, pasta_base_dados, caminho_base = encontrar_caminhos()
    
    print(f"📁 Pasta do Código:       {diretorio_script}")
    print(f"📁 Pasta Raiz (Projeto):  {diretorio_pai}")
    print(f"📁 Pasta Base de Dados:   {pasta_base_dados}")
    
    # ----------------------------------------------------
    # SPRINT 1: IMPORTAÇÃO E LEITURA DOS DADOS
    # ----------------------------------------------------
    if not caminho_base or not os.path.exists(caminho_base):
        print("\n[Erro Crítico] O arquivo da base de dados não foi encontrado na pasta 'Base de Dados'!")
        return
        
    try:
        df = pd.read_csv(caminho_base, sep=';', low_memory=False)
        print(f"\n[Sprint 1 - Sucesso] Base carregada de: {caminho_base}")
    except Exception as e:
        print(f"\n[Erro Crítico] Falha ao ler o arquivo CSV: {e}")
        return

    print(f"📊 Registros totais: {df.shape[0]:,} | Colunas: {df.shape[1]}")
    print("-" * 80)

    # ----------------------------------------------------
    # SPRINT 2 & 3: AUDITORIA E LIMPEZA DE DADOS
    # ----------------------------------------------------
    print("\n[Sprint 2 & 3] Auditoria de nulos, duplicatas e anomalias...")
    
    col_cat = 'PR_CAT' if 'PR_CAT' in df.columns else None
    if col_cat:
        qtd_nd = (df[col_cat] == '#N/D').sum()
        print(f"-> Anomalia detectada: {qtd_nd:,} ocorrências de '#N/D' na coluna '{col_cat}'.")

    if col_cat:
        def tratar_categorias(val):
            if pd.isna(val) or val == '#N/D':
                return "Sem Categoria"
            return str(val).strip()
        df[col_cat] = df[col_cat].apply(tratar_categorias)
        print(f"-> Coluna '{col_cat}' tratada (nulos e '#N/D' substituídos por 'Sem Categoria').")

    df = df.drop_duplicates()
    print(f"-> Duplicatas removidas. Linhas restantes: {df.shape[0]:,}")

    col_data = 'DATA' if 'DATA' in df.columns else None
    if col_data:
        df[col_data] = pd.to_datetime(df[col_data], errors='coerce')
        print(f"-> Coluna '{col_data}' convertida para datetime.")

    # SALVANDO O DATASET LIMPO ('df_limpo') EXATAMENTE DENTRO DA PASTA 'Base de Dados'
    os.makedirs(pasta_base_dados, exist_ok=True)
    caminho_saida_limpo = os.path.join(pasta_base_dados, "base_varejo_limpa.csv")
    df.to_csv(caminho_saida_limpo, index=False, sep=';')
    print(f"✨ [Arquivo Gerado] 'base_varejo_limpa.csv' salvo em:\n   {caminho_saida_limpo}")
    print("-" * 80)

    # ----------------------------------------------------
    # SPRINT 4: VALIDAÇÃO DA REGRA DE NEGÓCIO (CO_ID)
    # ----------------------------------------------------
    print("\n[Sprint 4] Validação da regra do identificador de compra...")
    col_id = 'CO_ID' if 'CO_ID' in df.columns else 'CO_ID'
    print(f"-> Total de itens (linhas): {df.shape[0]:,}")
    print(f"-> Total de transações únicas ({col_id}): {df[col_id].nunique():,}")
    print("-" * 80)

    # ----------------------------------------------------
    # SPRINT 5: ESTATÍSTICAS DESCRITIVAS (CL_FHL)
    # ----------------------------------------------------
    print("\n[Sprint 5] Estatísticas descritivas ('Número de Filhos - CL_FHL')...")
    col_filhos = 'CL_FHL' if 'CL_FHL' in df.columns else None
    
    if col_filhos:
        df[col_filhos] = pd.to_numeric(df[col_filhos], errors='coerce')
        s_filhos = df[col_filhos].dropna()
        print(f"  • Média: {s_filhos.mean():.4f} | Mediana: {s_filhos.median()} | Desvio Padrão: {s_filhos.std():.4f}")
        print(f"  • Máximo: {s_filhos.max()} | Mínimo: {s_filhos.min()} | Válidos: {s_filhos.count():,}")
    print("-" * 80)

    # ----------------------------------------------------
    # SPRINT 5: AGRUPAMENTOS E GRÁFICOS
    # ----------------------------------------------------
    print("\n[Sprint 5] Processando agrupamentos e gráficos...")
    
    col_genero = 'CL_GENERO' if 'CL_GENERO' in df.columns else None
    if col_genero:
        print(f"\n[Agrupamento 1] Itens por {col_genero}:\n{df.groupby(col_genero).size()}")

    if col_cat:
        top_cat = df.groupby(col_cat).size().sort_values(ascending=False).head(10)
        print(f"\n[Agrupamento 2] Top Categorias:\n{top_cat}")

    # GERAÇÃO DOS 4 GRÁFICOS NA PASTA RAIZ DO PROJETO ('graficos-varejo')
    if SALVAR_GRAFICOS:
        caminho_pasta_graficos = os.path.join(diretorio_pai, NOME_PASTA_GRAFICOS)
        os.makedirs(caminho_pasta_graficos, exist_ok=True)
        
        # Gráfico 1: Top 10 Categorias
        if col_cat:
            plt.figure(figsize=(12, 6))
            sns.barplot(x=top_cat.values, y=top_cat.index, palette="mako", hue=top_cat.index, legend=False)
            plt.title("Top 10 Categorias Mais Vendidas", fontsize=16, fontweight='bold', pad=15)
            plt.xlabel("Quantidade de Itens Vendidos", fontsize=12, fontweight='bold')
            plt.ylabel("Categoria", fontsize=12, fontweight='bold')
            plt.tight_layout()
            caminho_g1 = os.path.join(caminho_pasta_graficos, "grafico_top_categorias.png")
            plt.savefig(caminho_g1, dpi=300)
            plt.close()
            print(f"🎨 [1/4] Gráfico salvo: {caminho_g1}")

        # Gráfico 2: Distribuição de Filhos
        if col_filhos:
            plt.figure(figsize=(9, 5))
            sns.countplot(data=df, x=col_filhos, palette="crest", hue=col_filhos, legend=False)
            plt.title("Distribuição Demográfica: Número de Filhos", fontsize=16, fontweight='bold', pad=15)
            plt.xlabel("Número de Filhos", fontsize=12, fontweight='bold')
            plt.ylabel("Contagem de Clientes", fontsize=12, fontweight='bold')
            plt.tight_layout()
            caminho_g2 = os.path.join(caminho_pasta_graficos, "grafico_distribuicao_filhos.png")
            plt.savefig(caminho_g2, dpi=300)
            plt.close()
            print(f"🎨 [2/4] Gráfico salvo: {caminho_g2}")

        # Gráfico 3: Evolução Temporal de Vendas
        if col_data:
            df['ANO_MES'] = df[col_data].dt.to_period('M').astype(str)
            vendas_tempo = df.groupby('ANO_MES').size().tail(12)
            
            plt.figure(figsize=(14, 6))
            sns.lineplot(x=vendas_tempo.index, y=vendas_tempo.values, marker='o', color='#1f77b4', linewidth=2.5)
            plt.title("Evolução do Volume de Vendas por Período", fontsize=16, fontweight='bold', pad=15)
            plt.xlabel("Ano-Mês", fontsize=12, fontweight='bold')
            plt.ylabel("Total de Itens Vendidos", fontsize=12, fontweight='bold')
            plt.xticks(rotation=45)
            plt.tight_layout()
            caminho_g3 = os.path.join(caminho_pasta_graficos, "grafico_evolucao_vendas.png")
            plt.savefig(caminho_g3, dpi=300)
            plt.close()
            print(f"🎨 [3/4] Gráfico salvo: {caminho_g3}")

        # Gráfico 4: Distribuição por Gênero
        if col_genero:
            plt.figure(figsize=(8, 5))
            sns.countplot(data=df, x=col_genero, palette="Set2", hue=col_genero, legend=False)
            plt.title("Distribuição de Vendas por Gênero do Cliente", fontsize=16, fontweight='bold', pad=15)
            plt.xlabel("Gênero", fontsize=12, fontweight='bold')
            plt.ylabel("Quantidade de Itens", fontsize=12, fontweight='bold')
            plt.tight_layout()
            caminho_g4 = os.path.join(caminho_pasta_graficos, "grafico_genero_clientes.png")
            plt.savefig(caminho_g4, dpi=300)
            plt.close()
            print(f"🎨 [4/4] Gráfico salvo: {caminho_g4}")

    print("\n" + "="*80)
    print("✅ PIPELINE EXECUTADO COM SUCESSO TOTAL!")
    print("="*80)

if __name__ == "__main__":
    executar_pipeline_completo()