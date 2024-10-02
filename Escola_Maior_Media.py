import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_INSCRICAO','NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO','TP_ESCOLA'])

media_geral = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean().mean()/100

print(f"a média geral das Notas do ENEM 2020 É: {media_geral:.2f}")