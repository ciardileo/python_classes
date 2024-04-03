"""
Exercício geral de Numpy, pandas, matplotlib e seaborn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

# criação dos dados aleatórios
n = 1000
pct_smokers = 0.2

# cria um array de n números entre 0 e 1
flag_fumante = np.random.rand(n) < pct_smokers
# print(np.count_nonzero(flag_fumante == True))  # quantidade de fumantes gerados

# cria as variáveis do dataset
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# criação de um dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

# tratamento dos dados
dados['flag_fumante'] = dados['flag_fumante'].map(lambda x: "Fumante" if x == True else "Não Fumante")  # {True: "Fumante", False: "Não Fumante"}
# print(dados[0:1]) 

# gráfico
sea.set_style("ticks")

# cria um gráfico scatter com linha de regressão
sea.lmplot(data = dados, x = 'altura', y='peso', hue='flag_fumante', palette=['tab:blue', "tab:orange"], height=7)

# configura o gráfico
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre peso e altura entre fumantes e não fumantes')

# tira as bordas
sea.despine()

# cria uma grade
plt.grid()

# mostra o gráfico
plt.show()