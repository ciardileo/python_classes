"""
exercício 160
"""

import copy
import pprint as p

produtos = [
	{"nome": "Produto 1", "preço": 10},
	{"nome": "Produto 2", "preço": 105},
	{"nome": "Produto 3", "preço": 1014.10},
	{"nome": "Produto 4", "preço": 35.89},
]

# aumentando os preços em 10%
novos_produtos = [{'nome': produto['nome'], 'preço': produto['preço'] * 1.10} for produto in copy.deepcopy(produtos)]

p.pprint(novos_produtos)
print('=' * 25)

# ordenando em ordem decrescente de nome
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'], reverse=True)

p.pprint(produtos_ordenados_por_nome)
print('=' * 25)

# ordenando em ordem crescente de preço
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x['preço'])

p.pprint(produtos_ordenados_por_preco)
