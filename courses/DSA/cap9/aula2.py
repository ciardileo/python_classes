"""
arrays e funções
"""

import numpy as np

array2 = np.array([56, 89, 78, 23])

# funcões

print(array2.cumsum())  # soma acumulada

print(array2.cumprod())  # produto acumulado

a3 = np.arange(0, 100, 2)  # cria um array de 0 a 100 pulando de dois em dois
print(a3)

a4 = np.zeros((10, 2, 3))  # cria um array só de zeros
print(a4)

a5 = np.eye(4)  # cria uma matriz preenchida com 1 na diagonal
print(a5)

a6 = np.diag([2, 3, 4, 5, 6])  # cria uma matriz com certos elementos na diagonal
print(a6)

print(np.linspace(0, 10, 15))  # cria um vetor de números igual espaçados entre si até o 10

