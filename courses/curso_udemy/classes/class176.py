"""
funções builtin: map, filter e reduce
essas 3 funções úteis podem ser feitas com list comprehension
"""

from functools import reduce


# map - aplica uma função a cada valor de uma lista (pode ser feito com list comprehension)

def aumentar_preco(produto):
	return {**produto, 'preco': produto["preco"] * 1.5}


produtos = [
	{'produto': 'carro', 'preco': 600},
	{'produto': 'moto', 'preco': 200},
	{'produto': 'bike', 'preco': 50},
	{'produto': 'patinete', 'preco': 10},
]

print(*list(map(aumentar_preco, produtos)), sep='\n')  # a função recebe cada valor como argumento
print("=" * 25)

# filter - aplica uma função a todos os valores de um iterável, filtrando apenas os que retornam verdadeiro
print(*list(filter(lambda x: x['preco'] > 50, produtos)), sep='\n')
print("=" * 25)


# reduce - faz a redução de um iterável a um único valor (é a unica que precisa ser importada)

# def soma_precos(total, produto):  # o reduce serve nesse caso pra fazer a soma, para isso ele utiliza a variável
# 	# total, que será sempre o mesmo valor do return
# 	print(produto)
# 	return total + produto['preco']
#
#
# soma = reduce(soma_precos, produtos, 0)  # funcao, iterável, acumulador inicial
soma = reduce(lambda total, produto: total + produto['preco'], produtos, 0)  # forma mais simples de fazer com lambda

print(f"Soma total: {soma}")
