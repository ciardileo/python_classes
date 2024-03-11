"""
slicing
"""

import numpy as np

a1 = np.diag(np.arange(3, 30, 3))
a2 = np.diag(np.arange(3, 15))
print(a1)

print(a1[2])
print(a1[2, 3])
print(a1[:, 3])
print(a1[2:9:3])

# verifica se os dois arrays são iguais
print(np.array_equal(a1, a2))

# menor valor
print(a1.min())

# maior valor
print(a1.max())

# arredonda todos os valores
a3 = np.around(a1)

# adiciona 100 em todos os valores da matriz
a1 = a1 + 100
print(a1)

# transforma uma matriz multidimensional em unidimensional
a4 = a1.flatten()

# repete os elementos de um array
print(np.repeat(a4, 2))

# repete o array todo
print(np.tile(a4, 3))

# copia o array
a5 = np.copy(a4)



