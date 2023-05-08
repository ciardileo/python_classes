"""
lambdas: funções anônimas
sort e sorted()
a função sort consegue ordenar objetos simples em ordem crescente de numeros ou decrescente
podemos passar o parãmetro "key" em uma lambda para atribuir uma função a ela, essa função irá dizer
ao python por qual parâmetro os valores serão ordenados
"""

numeros = [2, 1, 3, 56, 4]
print(numeros.sort())
print(numeros.sort(reverse=True))  # ordena na ordem decrescente

lista = [
	{'nome': "Léo", "sobrenome": "Ciardi"},
	{'nome': "Enzo", "sobrenome": "Roma"},
	{'nome': "Marcos", "sobrenome": "Estranho"},
	{'nome': "Rodrigo", "sobrenome": "Divertido"},
]


lista.sort(key=lambda x: x['sobrenome'])  # nesse caso, passamos uma função anônima, o valor retornado é o que será usado para a ordenação
sorted(lista, key=lambda x: x['nome'])  # outra função que ordena lista, porém essa cria uma shallow copy da lista

for item in lista:
	print(item)
