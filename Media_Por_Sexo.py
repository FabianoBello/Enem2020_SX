import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO','TP_SEXO'])

# Calcular a média geral por sexo'TP_SEXO'
media_notas = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis=1)

# Agrupar por sexo e calcular a média geral
media_geral_por_sexo = media_notas.groupby(df['TP_SEXO']).mean()

print(media_geral_por_sexo)

# Calculando o TOTAL de resultados que cada QUESTAO,chegamos as MEDIAS GERAL POR SEXO:

TP_SEXO
F    518.18
M    529.86