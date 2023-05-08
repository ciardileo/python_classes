lista1 = [1, 2, 34, 55, 23, 1]
lista2 = [3, 4, 19, 32, 11]

lista_soma = [(x + y) for x, y in zip(lista2, lista1)]
print(lista_soma)