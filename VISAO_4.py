import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector


df = pd.read_csv('MICRODADOS_ENEM_2020.csv', sep = ';',encoding='ISO-8859-1')

import pandas as pd

# calculando as MEDIAS
medias_cn = df['NU_NOTA_CN'].mean()
medias_ch = df['NU_NOTA_CH'].mean()
medias_lc = df['NU_NOTA_LC'].mean()
medias_mt = df['NU_NOTA_MT'].mean()
medias_redacao = df['NU_NOTA_REDACAO'].mean()

# Calculate overall mean
media_geral = (medias_cn + medias_ch + medias_lc + medias_mt + medias_redacao) / 5

print("Mean of each note:")
print(f"NU_NOTA_CN: {medias_cn:.2f}")
print(f"NU_NOTA_CH: {medias_ch:.2f}")
print(f"NU_NOTA_LC: {medias_lc:.2f}")
print(f"NU_NOTA_MT: {medias_mt:.2f}")
print(f"NU_NOTA_REDACAO: {medias_redacao:.2f}")
print(f"Overall Mean: {media_geral:.2f}")

cnx = mysql.connector.connect(
    user='bello',
    password='teste123',
    host='127.0.0.1',
    database='enem__2020'
)

# Create a cursor object
cursor = cnx.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE TBL_NOTAS (
        id INT AUTO_INCREMENT,
        note VARCHAR(50),
        mean DECIMAL(5, 2),
        PRIMARY KEY (id)
    )
""")

cnx.commit()


cursor.close()
cnx.close()


# Insert the means into the table
cursor.execute("""
    INSERT INTO TBL_NOTAS (notas, medias) VALUES
        ('NU_NOTA_CN', %s),
        ('NU_NOTA_CH', %s),
        ('NU_NOTA_LC', %s),
        ('NU_NOTA_MT', %s),
        ('NU_NOTA_REDACAO', %s),
        ('MEDIA_GERAL', %s)
""", (medias_cn, medias_ch, medias_lc, medias_mt, medias_redacao,MEDIA_GERAL))

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
