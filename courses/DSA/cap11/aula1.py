"""
básicos de matplotlib
"""

import matplotlib.pyplot as plt

x, y = [1, 3, 5], [2, 4, 7]
w, z = [1, 6, 8], [1, 11, 12]

# define os eixos do gráfico
plt.plot(x, y, label='Variação')
plt.plot(w, z, label='Variação 2', color='red')

# configurações do gráfico
plt.xlabel("Variável 1")
plt.ylabel("Variável 2")
plt.title("Gráfico 1")
plt.legend()  # mostra o que estiver no label

# mostra o gráfico
plt.show()

