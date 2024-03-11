"""
estatística em numpy
"""

import numpy as np

a1 = np.array([10, 16, 12, 100, 44, 55, 94])

# média aritmética
print(np.mean(a1))

# desvio padrão: é uma medida de estatística que mostra o quanto os valores de um conjunto estão distantes da média
# desvio padrão baixo = valores variam pouco (desvio padrão é a raiz quadrada da variância)
print(np.std(a1))

# variância
print(np.var(a1))


