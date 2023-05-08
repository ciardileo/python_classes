"""
list comprehensions mais complexas

"""

# o código a seguir mostra loops for aninhados
lista = []
for x in range(3):
	for y in range(3):
		lista.append((x, y))

print(lista)

# versão com list comprehension
lista = [
	(x, y)
	for x in range(3)
	for y in range(3)
]

