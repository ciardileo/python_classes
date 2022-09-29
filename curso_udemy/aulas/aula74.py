"""
zip - une iteráveis, ex: une lista em ordem até a lista menor acabar
zip_longest (itertools) - igual ao zip, porém continua unindo até a lista mais longa acabar, caso não haja valor, ele retorna None no lugar
"""

from itertools import zip_longest

estados = ['SP', 'RJ', 'BA', 'ES']
cidades = ["São Paulo", "Rio de Janeiro", "Salvador", "Vitória", "Palmas"]

cidades_estados = zip(cidades, estados)  # retorna um iterador

for valor in cidades_estados:
	print(valor)

cidades_estados = list(zip_longest(cidades, estados, fillvalue="Desconhecido"))  # podemos trocar o none por algo personalizado

print(cidades_estados)


