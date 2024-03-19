"""
outras funções e métodos
"""

import pandas as pd

# importação de csv
df = pd.read_csv("assets/dataset.csv")

# filtro para saber se certos valores existem
print(df[df['Quantidade'].isin([3, 2, 1, 5, 6])])

# filtro com operadores lógicos (& e |)
print(df[(df.Segmento == 'Home Office') & (df.Regiao == 'South')].sample(5))  # o sample pega valores de forma aleatória

# agrupamento (agrupa pelas colunas que queremos trabalhar, agrupamos pelas colunas não númericas)
print(df[['Regiao', 'Segmento', 'Quantidade']].groupby(['Segmento', 'Regiao']).mean())
print('=' * 60)
# o agg() serve para retornar diversos cálculos diferentes sobre a coluna valor_venda
print(df[['Regiao', 'Segmento', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))
