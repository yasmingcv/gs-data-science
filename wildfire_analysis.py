# wildfire_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# Configurações gerais de visualização
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Defina sua SEED (exemplo: somatório do último dígito das matrículas do grupo)
SEED = 42
SAMPLE_SIZE = 500_000
DATASET_PATH = "wildfires.csv"  # certifique-se que o CSV está no mesmo diretório

def carregar_dados(caminho_csv):
    print("Carregando dados...")
    df = pd.read_csv(caminho_csv, low_memory=False)
    print(f"Total de registros carregados: {len(df)}")
    return df

def limpar_dados(df):
    print("\nLimpando dados...")
    df = df.drop_duplicates()

    # Tratamento de campos de data
    df['DISCOVERY_DATE'] = pd.to_datetime(df['DISCOVERY_DATE'], errors='coerce')
    df['CONT_DATE'] = pd.to_datetime(df['CONT_DATE'], errors='coerce')

    # Remoção de outliers extremos de área
    df = df[df['FIRE_SIZE'] < df['FIRE_SIZE'].quantile(0.99)]

    # Preenchimento de nulos com 'Desconhecido'
    df['NWCG_CAUSE_CLASSIFICATION'] = df['NWCG_CAUSE_CLASSIFICATION'].fillna('Desconhecida')
    df['NWCG_GENERAL_CAUSE'] = df['NWCG_GENERAL_CAUSE'].fillna('Desconhecida')

    print(f"Total de registros após limpeza: {len(df)}")
    return df

def amostrar_dados(df, seed, n=500_000):
    print(f"\nAmostrando {n} registros com seed {seed}...")
    return df.sample(n=n, random_state=seed)

def analise_descritiva(df):
    print("\nResumo estatístico das áreas queimadas:")
    print(df['FIRE_SIZE'].describe())

    print("\nFrequência por tipo de causa:")
    print(df['NWCG_CAUSE_CLASSIFICATION'].value_counts())

    print("\nEstados com mais incêndios:")
    print(df['STATE'].value_counts().head(10))

def gerar_graficos(df):
    print("\nGerando gráficos...")

    # 1. Incêndios por ano
    plt.figure()
    df.groupby('FIRE_YEAR').size().plot(kind='line')
    plt.title('Incêndios por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade')
    plt.savefig('grafico_incendios_por_ano.png')

    # 2. Mapa de calor de localização dos incêndios
    plt.figure()
    sns.kdeplot(x=df['LONGITUDE'], y=df['LATITUDE'], cmap="Reds", fill=True, bw_adjust=1)
    plt.title("Mapa de Calor dos Incêndios")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig('grafico_mapa_calor.png')

    # 3. Incêndios por estado (Top 10)
    top_causas = df['NWCG_GENERAL_CAUSE'].value_counts().nlargest(10)
    sns.barplot(x=top_causas.values, y=top_causas.index, color='steelblue')
    plt.title('Top 10 Causas Gerais dos Incêndios')
    plt.xlabel('Número de Incêndios')
    plt.ylabel('Causa Geral')
    plt.tight_layout()
    plt.savefig('grafico_top_10_causas.png')

    # 4. Relação entre causa (Humana/Natural) e tamanho do incêndio
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[df['NWCG_CAUSE_CLASSIFICATION'].isin(['Human', 'Natural'])],
                x='NWCG_CAUSE_CLASSIFICATION', y='FIRE_SIZE')
    plt.yscale('log')  # Escala logarítmica para melhor visualização
    plt.title('Tamanho dos Incêndios por Classificação da Causa (Humana vs Natural)')
    plt.xlabel('Classificação da Causa')
    plt.ylabel('Tamanho do Incêndio (acres) - escala log')
    plt.savefig('grafico_tamanho_por_classificacao_causa.png')

    # Garante que a data está no formato datetime
    df['DISCOVERY_DATE'] = pd.to_datetime(df['DISCOVERY_DATE'], errors='coerce')

    # Extrai o mês (como número e nome abreviado)
    df['month'] = df['DISCOVERY_DATE'].dt.month

    # Mapeia o número do mês para nome
    month_names = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    df['month_name'] = df['month'].map(month_names)

    # Conta incêndios por mês e ordena corretamente
    month_order = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    fires_by_month = df['month_name'].value_counts().reindex(month_order)

    # 5. Gráfico de barras do número de incêndios por mês
    plt.figure(figsize=(12, 6))
    sns.barplot(x=fires_by_month.index, y=fires_by_month.values, color='tomato')
    plt.title('Número de Incêndios por Mês do Ano')
    plt.xlabel('Mês')
    plt.ylabel('Número de Incêndios')
    plt.tight_layout()
    plt.savefig('grafico_incendios_por_mes.png')
    plt.show()

    print("Gráficos salvos como arquivos PNG.")

def main():
    df = carregar_dados(DATASET_PATH)
    df = limpar_dados(df)
    df_amostra = amostrar_dados(df, SEED, SAMPLE_SIZE)
    analise_descritiva(df_amostra)
    gerar_graficos(df_amostra)
    print("\nAnálise finalizada.")

if __name__ == "__main__":
    main()
