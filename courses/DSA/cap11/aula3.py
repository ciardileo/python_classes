"""
gráficos personalizados de pylab
"""

import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0, 5, 10)
y = x ** 2

# um gráfico dentro de outro
fig = plt.figure()

# criação e configuração do gráfico 1
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # escala dos valores (esquerda, inferior, largura, altura) (de 0 a 1)
axes1.plot(x, y, "r")  # r é red
axes1.set_xlabel("X")
axes1.set_ylabel("Y")
axes1.set_title("Gráfico de Linha")

# criação e congiguração do gráfico 2
axes2 = fig.add_axes([0.2, 0.52, 0.4, 0.3])  # escala dos valores
axes2.plot(y, x, "g") 
axes2.set_xlabel("Y")
axes2.set_ylabel("X")
axes2.set_title("Gráfico de Linha 2")

plt.show()