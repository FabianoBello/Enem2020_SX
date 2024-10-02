import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1')

# Assume 'df' é o seu DataFrame contendo as notas e os resultados dos questionários

# Gráfico de barras empilhadas
fig, ax = plt.subplots(figsize=(12, 6))
for i, nota in enumerate(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']):
    ax.bar(df['Q001'], df[nota], label=nota)
    ax.bar(df['Q002'], df[nota], label=nota)
    # ...
    ax.bar(df['Q025'], df[nota], label=nota)
ax.set_xlabel('Questionário')
ax.set_ylabel('Nota')
ax.set_title('Gráfico de barras empilhadas')
ax.legend()
plt.show()

# Gráfico de dispersão com linhas de tendência
fig, axs = plt.subplots(5, 1, figsize=(12, 12))
for i, nota in enumerate(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']):
    axs[i].scatter(df['Q001'], df[nota])
    axs[i].scatter(df['Q002'], df[nota])
    # ...
    axs[i].scatter(df['Q025'], df[nota])
    axs[i].plot(df['Q001'], df[nota], label=nota)
    axs[i].plot(df['Q002'], df[nota], label=nota)
    # ...
    axs[i].plot(df['Q025'], df[nota], label=nota)
    axs[i].set_xlabel('Questionário')
    axs[i].set_ylabel('Nota')
    axs[i].set_title(f'Gráfico de dispersão com linhas de tendência para {nota}')
    axs[i].legend()
plt.show()

# Gráfico de radar
fig, ax = plt.subplots(figsize=(12, 6), subplot_kw=dict(polar=True))
for i, nota in enumerate(['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']):
    ax.plot(df['Q001'], df[nota], label=nota)
    ax.plot(df['Q002'], df[nota], label=nota)
    # ...
    ax.plot(df['Q025'], df[nota], label=nota)
ax.set_xlabel('Questionário')
ax.set_ylabel('Nota')
ax.set_title('Gráfico de radar')
ax.legend()
plt.show()
