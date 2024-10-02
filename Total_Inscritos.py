import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_INSCRICAO'])

total_inscritos = len(df.index)

print(f"O numero TOTAL de inscritos no ENEM 2020 É : {total_inscritos}")

# usando o INDEX, totalizamos: 57.831.09  inscritos
