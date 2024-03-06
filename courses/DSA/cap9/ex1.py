"""
Criar uma matriz de zeros com dimensões 3x3.
Criar uma matriz de uns com dimensões 4x2.
Criar uma matriz identidade 4x4.
Criar um array de números inteiros de 0 a 9.
Criar um array de números inteiros de 1 a 20, pulando de 2 em 2.
Criar uma matriz 3x3 com valores aleatórios entre 0 e 1.
Somar duas matrizes de mesma dimensão.
Multiplicar duas matrizes.
Calcular a transposta de uma matriz.
Calcular a média de todos os elementos em uma matriz.
"""

import numpy as np

# ex1
m1 = np.zeros((3, 3))
print(m1)

# ex2
m2 = np.ones((4, 2))
print(m2)

# ex3
m3 = np.eye(4)
print(m3)

# ex4
a1 = np.arange(10)
print(a1)

# ex5
a2 = np.arange(1, 20, 2)
print(a2)

# ex6
m4 = np.random.rand(3, 3)
print(m4)

# ex7
soma = a1 + a2
print(soma)

# ex8
produto = a1 * a2
print(produto)

# ex9
print(m2.T)

# ex10
media = np.mean(m4)
print(media)
