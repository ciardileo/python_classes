"""
Fundamentos da Estatística:
- Entender a pergunta de negócio;
- Achar a variável alvo;
- Achar a(s) variável(is) preditoras;
- Escolher um modelo estatístico adequado;
- Obter dados históricos;
- Treinar o modelo.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

df = pd.read_csv('./dataset.csv')


# passo a passo de resumo estatístico descritivo:

# verificação de valores ausentes
print(df.isnull().sum())

# descrição dos valores
print(df.describe())

# descrição de valores específicos: variável alvo
print(df['valor_aluguel'].describe())

# histograma - gráfico que mostra a frequência de cada intervalo de valores
sns.histplot(data=df, x = 'valor_aluguel', kde=True)
plt.show()

# correlação entre as variáveis - correlação de pearson
print(df.corr()) # podemos ver que a variável que está mais correlacionada com o aluguel é a área, logo escolhemos ela como variável preditora

# gráfico de pontos
sns.scatterplot(data=df, x='area_m2', y='valor_aluguel')
plt.show()

