"""
preenchimento de valores ausentes
"""

import pandas as pd

# importação de csv
df = pd.read_csv("assets/dataset.csv")

print(df.head(10))

# moda: valor mais frequente
moda = df['Quantidade'].value_counts().index[0]

# preenchimento de campos vazios
df['Quantidade'].fillna(value=moda, inplace=True)  # inplace salva no próprio dataframe
print(df.head())