"""
Criação de Modelos Estatísticos
"""

import pandas as pd
import statsmodels.api as sm

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

