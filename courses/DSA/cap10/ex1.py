"""
exercícios misturando numpy e pandas
"""

import numpy as np
import pandas as pd

# ex 1

df = pd.DataFrame(np.random.randint(0, 100, size=(5, 3)), columns=['N1', 'N2', 'N3'])
print(df)
print(f"A média da coluna N1 é {df['N1'].mean()} e seu desvio padrão é {df['N1'].std()}")

# ex 2

# Criar uma matriz NumPy com dados aleatórios
matriz = np.random.randn(5, 3)

# Calcular o desvio padrão de cada linha
desvio_padrao_linhas = np.std(matriz, axis=1)

# Criar um DataFrame Pandas com a matriz e adicionar o desvio padrão como nova coluna
df = pd.DataFrame(matriz, columns=['A', 'B', 'C'])
df['Desvio_Padrao'] = desvio_padrao_linhas
print(df)

# ex 3
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Calcular o desvio padrão ao longo das linhas (para cada coluna)
std_por_coluna = df.std(axis=0)
print("Desvio padrão por coluna:\n", std_por_coluna)

# Calcular o desvio padrão ao longo das colunas (para cada linha)
std_por_linha = df.std(axis=1)
print("\nDesvio padrão por linha:\n", std_por_linha)