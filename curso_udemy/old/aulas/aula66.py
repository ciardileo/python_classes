"""
List comprehension
são semelhantes a lambdas
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex = [valor * 2 for valor in l1]  # itera a primeia lista retornando o dobro de cada valor
print(ex)

# =========================================================

ex2 = [(f'Pos: {v2}', f'Val: {v}') for v in l1 for v2 in range(len(l1))]  # podemos usar mais de uma variavel na list comprehension
print(ex2)

# =========================================================

l1 = list(range(100))
ex3 = [v if v % 2 == 0 else -1 for v in l1]  # podemos usar condições
