import pandas as pd

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT'])

# Contar o total de alunos com falta em cada disciplina
faltas_cn = (df['TP_PRESENCA_CN'] == 0).sum()
faltas_ch = (df['TP_PRESENCA_CH'] == 0).sum()
faltas_lc = (df['TP_PRESENCA_LC'] == 0).sum()
faltas_mt = (df['TP_PRESENCA_MT'] == 0).sum()

# Calcular o total de alunos com falta
total_faltas = faltas_cn + faltas_ch + faltas_lc + faltas_mt

# Calcular o percentual de faltas
total_alunos = len(df)
percentual_faltas = (total_faltas / total_alunos) * 100

print("Total de alunos com falta:", total_faltas)
print("Percentual de faltas:", f"{percentual_faltas:.2f}%")

# De acordo com a CONTAGEM e totalizacao dos campos de presença iguais a zero, chegamos ao total de :
#absenteismo GERAL.

#Absenteismo  :: Percentual de faltas: 214.72%
#