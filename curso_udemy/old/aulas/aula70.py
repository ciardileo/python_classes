"""
Geradores, iteradores e iteráveis
Objetos iteráveis basicamente, podem ser usados com o for, possuem índices e podem ser passados um por um em seus valores, como strings, listas, etc
O iterador é um objeto que so pode nos dar seus valores um de cada vez, é no que as listas no for são transformadas para poderem ser iteradas
Os geradores são um tipo especial de iterador que para poupar memória, não carregam os valores de "primeira", o valor só é carregado quando for chamado,
normalmente usado nas funções, possui uma função especial chamada "yield" que serve como um "return", mas que não para a execução e faz essa função de memória
geradores podem ser criados por meio de uma comprehension entre parenteses
"""

# =========================================================
# iteráveis

lista = [0, 1, 2, 3, 4, 5]
string = "Leonardo"
num = 1244

for item in lista:
	print(item)

for letra in string:
	print(letra)

"""
Isso causará um erro, pois um int não é iteravel, não possui "casas/índice"
for algarismo in num:
	print(algarismo)
"""

# =========================================================
# iteradores

lista2 = [0, 3, 4, 5, 6]
lista2 = iter(lista2)

print(lista2)
print(next(lista2))


# =========================================================
# geradores

def gerar():  # também podemos criar um gerador por meio de uma função
	for i in range(100000):
		yield i


gerador = gerar()
print(gerador)
for a in gerador:
	print(a)

gerador = (x for x in range(10000))  # podemos criar um gerador por meio de uma comprehension
for i in gerador:
	print(i)


