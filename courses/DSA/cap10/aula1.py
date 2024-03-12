"""
básicos do pandas e dataframes
"""

import pandas as pd

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'Idade': [25, 30, 21, 28, 35],
    'Gênero': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
    'Altura': [1.75, 1.65, 1.80, 1.70, 1.85],
    'Peso': [70, 60, 80, 55, 90]
}

# cria um dataframe/tabela com a opção de organizar as colunas
dataframe = pd.DataFrame(dados, columns=['Nome', 'Gênero', 'Idade', 'Peso', 'Altura'])

# mostra as 5 primeiras linhas
print(dataframe.head())
print('=' * 25)

# podemos adicionar colunas que não estão na base de dados e também mudar o índice
dataframe = pd.DataFrame(dados, columns=['Nome', 'Idade', 'Peso', 'Altura', 'Profissão'], index=['P1', 'P2', 'P3', 'P4', 'P5'])

print(dataframe.head())
print('=' * 25)

print(dataframe.values)

# tipos de cada coluna
print(dataframe.dtypes)

print(dataframe.columns)
print('=' * 25)

# fatiamento
print(dataframe[["Nome", "Idade"]])
print('=' * 25)

# filtros
print(dataframe.filter(items=['P2'], axis=0))
