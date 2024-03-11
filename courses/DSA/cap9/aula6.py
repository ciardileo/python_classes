"""
operações matemáticas
"""

import numpy as np

a1 = np.arange(1, 10)
a2 = np.arange(11, 20)

# soma total
print(np.sum(a1))

# produto total
print(np.prod(a1))

# soma acumulada
print(np.cumsum(a1))

# produto acumulado
print(np.cumprod(a1))

# adição de dois arrays
a3 = np.add(a1, a2)

# multiplicação de dois arrays (num cols da primeira matriz = num linhas da segunda matriz)
a4 = np.prod(a1, a2)
a4 = a1 @ a2
