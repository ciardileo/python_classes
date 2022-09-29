"""
Dictionary comprehension
similar ao list comprehension, mas deve ter o ":" de chave e valor
caso nao possua o ":", vira um set comprehension
"""

lista = [
	(1, 2),
	(4, 8),
]

dictionary = {f"Chave: {x}": f"Valor: {y}" for x, y in lista}
print(dictionary)
