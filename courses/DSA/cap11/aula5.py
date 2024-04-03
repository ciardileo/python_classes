""" 
histogramas
"""

import matplotlib.pyplot as plt
import numpy as np

dados = np.random.randn(10000)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# plot 1
axes[0].hist(dados)
axes[0].set_title("Histograma padrão")
axes[0].set_xlim(min(dados), max(dados))

# plot 1
axes[0].hist(dados, cumulative=True, bins=50)
axes[0].set_title("Histograma padrão")
axes[0].set_xlim(min(dados), max(dados))