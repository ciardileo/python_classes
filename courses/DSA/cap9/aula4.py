"""
arquivos
"""

import os
import numpy as np

# caminho do arquivo
file = os.path.join("assets/dataset.csv")

# importamos os dados de um arquivo csv para criar um array
a1 = np.loadtxt(file, delimiter=',', usecols=(0, 1, 2, 3), skiprows=1)  # use cols - colunas a mostrar, skiprows - linhas a pular

print(a1)
