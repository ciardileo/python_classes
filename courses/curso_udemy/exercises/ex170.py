"""
exercício - soma de duas listas
"""

lista1 = [1, 3, 4, 5, 6, 7]
lista2 = [2, 1, 5]

lista_somada = [x + y for x, y in list(zip(lista1, lista2))]
print(lista_somada)