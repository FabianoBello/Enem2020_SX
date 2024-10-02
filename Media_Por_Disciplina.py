import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'])

# Calcular a média por disciplina
media_cn = df['NU_NOTA_CN'].mean()
media_ch = df['NU_NOTA_CH'].mean()
media_lc = df['NU_NOTA_LC'].mean()
media_mt = df['NU_NOTA_MT'].mean()
media_redacao = df['NU_NOTA_REDACAO'].mean()

print(f"Média em Ciências Naturais (CN): {media_cn:.2f}")
print(f"Média em Ciências Humanas (CH): {media_ch:.2f}")
print(f"Média em Linguagens e Códigos (LC): {media_lc:.2f}")
print(f"Média em Matemática (MT): {media_mt:.2f}")
print(f"Média em Redação: {media_redacao:.2f}")

# Calculando o TOTAL de resultados que cada QUESTAO,chegamos as MEDIAS abaixo:

#Média em Ciências Naturais (CN): 490.41
#Média em Ciências Humanas (CH): 511.15
#Média em Linguagens e Códigos (LC): 523.80
#Média em Matemática (MT): 520.58
#Média em Redação: 573.41