"""
mais personalização de gráficos
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 25)
y = np.sin(x)  # seno de cada elemento de x

# divide a área em dois subplots - retorna a figura e um array numpy com os axes
fig, axes = plt.subplots(nrows=2, ncols=2)

# cria cada gráfico
for ax in axes.flat:  # tranforma o array de matriz 2,2 para vetor de 4
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(color='b', alpha=0.7, linestyle='dashed', linewidth=0.8)
    # ax.set_yscale('log')  # define uma secola logaritmica
    ax.set_title(f'Título {np.where(axes.flat == ax)[0][0] + 1}')
        
fig.tight_layout()
plt.show()
