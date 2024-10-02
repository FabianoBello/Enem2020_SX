import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_INSCRICAO','NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO','TP_ESCOLA'])

total_absences = (df[['TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT']] == 0).sum().sum()


total_students = df.shape[0]


total_absence_percentage = (total_absences / total_students) * 100

print(f"% de Ausentes: {total_absence_percentage:.2f}%")

# De acordo com a soma dos campos de presença iguais a zero, chegamos ao total de :
#absenteismo GERAL.

#a MÉDIA GERAL é 523.87
#