"""
gráficos em pandas
possui gráficos simples
"""

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# importação de csv
data = load_iris()

# cria um DataFrame a partir de um dataset do sckit learn
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['species'] = data['target']

# gráficos com matplotlib inline
df.plot()
plt.show()

df.groupby('species').mean().plot.bar()
plt.show()