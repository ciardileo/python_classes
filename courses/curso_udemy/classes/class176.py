"""
funções builtin: map, filter e reduce
"""


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
