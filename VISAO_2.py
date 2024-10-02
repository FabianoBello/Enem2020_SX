import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1',usecols=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'])

fig, axs = plt.subplots(2, 2, figsize=(12, 12))
for i, notas in enumerate(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']):
    sns.regplot(x=df[notas], y=df['NU_NOTA_REDACAO'], ax=axs[i//2, i%2])
    axs[i//2, i%2].set_title(f"{notas} vs. NU_NOTA_REDACAO")
    axs[i//2, i%2].set_xlabel(notas)
    axs[i//2, i%2].set_ylabel('NU_NOTA_REDACAO')
plt.show()


corr_matrix = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title("Correlation Matrix")
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='NU_NOTA_CN', y='NU_NOTA_REDACAO', data=df)
sns.boxplot(x='NU_NOTA_CH', y='NU_NOTA_REDACAO', data=df)
sns.boxplot(x='NU_NOTA_LC', y='NU_NOTA_REDACAO', data=df)
sns.boxplot(x='NU_NOTA_MT', y='NU_NOTA_REDACAO', data=df)
ax.set_xlabel("notas")
ax.set_ylabel('NU_NOTA_REDACAO')
plt.show()
