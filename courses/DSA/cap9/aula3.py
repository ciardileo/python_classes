"""
matrizes
"""

import numpy as np

a1 = np.ones((2, 3))  # preenche um objeto com números 1
print(a1)

lista = [[2, 3, 4], [2, 3, 1], [1, 3, 44]]
a2 = np.matrix(lista, dtype=np.float64)  # cria uma matriz
print(a2)

print(a2.size)  # qtd de células

print(a2.itemsize)  # retorna o tamanho em bytes de cada elemento do array

print(a2.nbytes)  # tamanho em bytes do array

print(a2.ndim)  # número de dimensões