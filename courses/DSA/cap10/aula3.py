"""
slicing de dataframes
"""

import pandas as pd


dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'Idade': [25, 30, 21, 28, 35],
    'Gênero': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
    'Altura': [1.75, 1.65, 1.80, 1.70, 1.85],
    'Peso': [70, 60, 80, 55, 90]
}

df = pd.DataFrame(dados, columns=['Nome', 'Idade', 'Peso', 'Altura', 'Nível'])

print(df[0:4])  # slicing por index (não é exclusivo, diferente do numpy)

print(df[df['Idade'] > 25])  # slicing com condição

print(df[['Nome', 'Idade']])
