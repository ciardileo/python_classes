"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import permutations, combinations, product

pessoas = ["Luiz", "André", "Eduardo", "Letícia", "Fabrício", "Rose"]

for grupo in combinations(pessoas, 2):  # valores, número de posições
	print(grupo)

# =======================================================================

for grupo in permutations(pessoas, 3):
	print(grupo)

# =======================================================================

for grupo in product(pessoas, repeat=2):
	print(grupo)

print(len(list(permutations(pessoas, 3))))  # quantidade de permutações