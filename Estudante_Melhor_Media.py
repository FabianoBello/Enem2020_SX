import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_INSCRICAO')

total_enrolled_students = df['NU_INSCRICAO'].sum()

print(f"Total number of enrolled students: {total_enrolled_students}")

# usando a coluna NU_INSCRITOS, totalizamos:
