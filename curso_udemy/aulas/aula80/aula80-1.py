"""
map - aplica uma função a cada item de uma lista
"""

from aula80 import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)  # função, valores
print(list(nova_lista))


# =============================================================

def aumenta_preco(p):
	p['preço'] = round(p['preço'] * 1.05, 2)
	return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
	print(produto)

# =============================================================

nomes = map(lambda p: p['idade'] * 2, pessoas)

print(list(nomes))
