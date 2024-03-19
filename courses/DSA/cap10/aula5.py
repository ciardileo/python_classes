"""
queries em pandas
"""

import pandas as pd

# importação de csv
df = pd.read_csv("assets/dataset.csv")

# cria um novo dataframe com esse filtro
df2 = df.query('Valor_Venda > 400')
print(df2)