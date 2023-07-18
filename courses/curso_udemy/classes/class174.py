"""
ANÁLISE COMBINATÓRIA
combinações, permutações e produto
combinação = ordem não importa
permutação = ordem importa
produto = ordem importa e repete valores únicos (combina valores - princípio multiplicativo)
"""

from itertools import combinations, permutations, product

pessoas = ["Léo", "Renato", "João", "Júlia"]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['normal', 'oversized']
]

# retorna um iterator
combinacao = combinations(pessoas, 2)  # segundo argumento é o tamanho do grupo
permutacao = permutations(pessoas, 2)  # `
produto = product(*camisetas)

print(*list(combinacao), sep='\n')
print("=" * 25)
print(*list(permutacao), sep='\n')
print('=' * 25)
print(*list(produto), sep='\n')
