"""
Criação de Modelos Estatísticos
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Carregar o DataFrame
df = pd.read_csv('./dataset.csv')

# Variável dependente
y = df['valor_aluguel']

# Variáveis independentes
X = df[['area_m2', 'numero_banheiros', 'numero_cozinhas', 'ano_construcao']]

# Adicionar constante
X = sm.add_constant(X)

# Criar modelo de regressão linear múltipla
model = sm.OLS(y, X)

# Treinar o modelo
resultado = model.fit()

# Imprimir resultados
print(resultado.summary())

# gráfico
plt.figure(figsize=(12, 8))
plt.xlabel('area_m2')
plt.ylabel('valor_aluguel')
plt.plot(X['area_m2'], y, 'o', label='Dados Reais')
plt.plot(X['area_m2'], resultado.fittedvalues, 'r-', label='Linha de Regressão')
plt.legend(loc='best')
plt.show()