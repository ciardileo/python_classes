""" 
básicos Seaborn
"""

import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sea 

# loading dataset
dados = sea.load_dataset('tips')
print(dados.head())

sea.jointplot(data=dados, x='total_bill', y='tip', kind='reg')

sea.lmplot(data=dados, x='total_bill', y='tip', col='smoker')

plt.show()

# creating data
df = pd.DataFrame()
df['idade'] = random.sample(range(20, 90), 30)
df['peso'] = random.sample(range(40, 150), 30)

# cria um gráfico de dispersão com uma linha de regressão, que mostra a média de peso por idade e a relação entre os dois. A área com sombra é uma margem de erro
sea.lmplot(data = df, x = 'idade', y='peso', fit_reg=True)