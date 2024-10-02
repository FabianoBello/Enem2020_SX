import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO','TP_COR_RACA'])

# Calcular a média geral por sexo'TP_SEXO'
media_notas = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis=1)

# Criar um dicionário para mapear os códigos de raca

raca_nome = {
    0: 'Não declarado',
    1: 'Branca',
    2: 'Preta',
    3: 'Parda',
    4: 'Amarela',
    5: 'Indígena'
}

# Calcular a média por raca
for raca in df['TP_COR_RACA'].unique():
    media_cn = df[df['TP_COR_RACA'] == raca]['NU_NOTA_CN'].mean()/100
    media_ch = df[df['TP_COR_RACA'] == raca]['NU_NOTA_CH'].mean()/100
    media_lc = df[df['TP_COR_RACA'] == raca]['NU_NOTA_LC'].mean()/100
    media_mt = df[df['TP_COR_RACA'] == raca]['NU_NOTA_MT'].mean()/100
    media_redacao = df[df['TP_COR_RACA'] == raca]['NU_NOTA_REDACAO'].mean()/100
    
    print(f"Média em Ciências Naturais (CN) - {raca_nome[raca]}: {media_cn:.2f}")
    print(f"Média em Ciências Humanas (CH) - {raca_nome[raca]}: {media_ch:.2f}")
    print(f"Média em Linguagens e Códigos (LC) - {raca_nome[raca]}: {media_lc:.2f}")
    print(f"Média em Matemática (MT) - {raca_nome[raca]}: {media_mt:.2f}")
    print(f"Média em Redação - {raca_nome[raca]}: {media_redacao:.2f}")
    print()

# Calculando o TOTAL de resultados por ETNIA ::

Média em Ciências Naturais (CN) - Preta: 4.71
Média em Ciências Humanas (CH) - Preta: 4.91
Média em Linguagens e Códigos (LC) - Preta: 5.10
Média em Matemática (MT) - Preta: 4.86
Média em Redação - Preta: 5.35

Média em Ciências Naturais (CN) - Parda: 4.77
Média em Ciências Humanas (CH) - Parda: 4.95
Média em Linguagens e Códigos (LC) - Parda: 5.10
Média em Matemática (MT) - Parda: 4.99
Média em Redação - Parda: 5.50

Média em Ciências Naturais (CN) - Branca: 5.13
Média em Ciências Humanas (CH) - Branca: 5.38
Média em Linguagens e Códigos (LC) - Branca: 5.45
Média em Matemática (MT) - Branca: 5.58
Média em Redação - Branca: 6.15

Média em Ciências Naturais (CN) - Não declarado: 5.00
Média em Ciências Humanas (CH) - Não declarado: 5.22
Média em Linguagens e Códigos (LC) - Não declarado: 5.29
Média em Matemática (MT) - Não declarado: 5.31
Média em Redação - Não declarado: 5.72

Média em Ciências Naturais (CN) - Amarela: 4.91
Média em Ciências Humanas (CH) - Amarela: 5.06
Média em Linguagens e Códigos (LC) - Amarela: 5.20
Média em Matemática (MT) - Amarela: 5.23
Média em Redação - Amarela: 5.71

Média em Ciências Naturais (CN) - Indígena: 4.53
Média em Ciências Humanas (CH) - Indígena: 4.66
Média em Linguagens e Códigos (LC) - Indígena: 4.82
Média em Matemática (MT) - Indígena: 4.63
Média em Redação - Indígena: 4.89