"""
manipulação de dataframes
"""

import pandas as pd
import numpy as np

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'Idade': [25, 30, 21, 28, 35],
    'Gênero': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
    'Altura': [1.75, 1.65, 1.80, 1.70, 1.85],
    'Peso': [70, 60, 80, 55, 90]
}

df = pd.DataFrame(dados, columns=['Nome', 'Idade', 'Peso', 'Altura', 'Nível'])

# resumo estatístico de colunas numéricas
print(df.describe())

# indica onde tem valores ausentes no dataframe
print(df.isna())

# preenchendo parte vazia do dataframe com numpy
df['Nível'] = np.arange(5.)
