"""
Sintaxe SQL no Pandas
"""

import sqlite3 as sql
import pandas as pd

# conexão
con = sql.connect("database.db")
cursor = con.cursor()

# criação do dataframe
cursor.execute("SELECT * FROM tb_vendas_dsa")
dados = cursor.fetchall()
df = pd.DataFrame(dados, columns=[description[0] for description in cursor.description])
print(df.sample(5))

# média
print(df['Unidades_Vendidas'].mean())

# contagem de valores
print(df.value_counts())

# fechamento
cursor.close()
con.close()
