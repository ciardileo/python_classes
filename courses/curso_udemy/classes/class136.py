"""
list comprehension - maneira rápida de criar listas em python
map e filter
"""

lista = []
for numero in range(10):
	lista.append(numero * 2)

print(lista)

# versão com list comprehension
lista = [n * 2 for n in range(10)]
print(lista)

# mapeamento de dados (função map) ===========================================
produtos = [
	{'nome': 'p1', 'preço': 20, },
	{'nome': 'p2', 'preço': 50, },
	{'nome': 'p3', 'preço': 60, },
	{'nome': 'p4', 'preço': 15, },
]

produtos_caros = [
	{'nome': produto['nome'], 'preço': produto['preço'] * 1.75} for produto in produtos
]  # exemplo criando um dicionário

produtos_caros = [
	{**produto, 'preço': produto['preço'] * 1.75} if produto['preço'] > 20 else {**produto} for produto in produtos
]  # exemplo com if ternário

print(produtos_caros)

# filtro de dados (função filter) =============================================

produtos_caros = [
	{**produto, 'preço': produto['preço'] * 1.75} for produto in produtos if produto['preço'] > 18
]  # exemplo de filtro, que tem o IF depois do FOR

