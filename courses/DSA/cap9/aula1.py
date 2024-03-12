"""
arrays
"""

import numpy as np

# cria um array
array1 = np.array([10, 23, 10, 344, 53, 21])

# formato do array (podem ser multidimensionais)
print(array1.shape)

# tipo de dado
print(array1.dtype)


# fatiamento e alteração
array1[0] = 12
print(array1[2:4])



