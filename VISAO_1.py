import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'])

fig, axs = plt.subplots(1, 5, figsize=(20, 4))
for i, notas in enumerate(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']):
    axs[i].hist(df[notas], bins=50)
    axs[i].set_title(notas)
    axs[i].set_xlabel('Valor das Notas')
    axs[i].set_ylabel('Frequência')
plt.show()


fig, axs = plt.subplots(5, 5, figsize=(20, 20))
for i, notas1 in enumerate(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']):
    for j, notas2 in enumerate(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']):
        axs[i, j].scatter(df[notas1], df[notas2])
        axs[i, j].set_xlabel(notas1)
        axs[i, j].set_ylabel(notas2)
plt.show()


fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([df[notas] for notas in ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']])
ax.set_xticklabels(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'])
ax.set_ylabel('notas Value')
plt.show()