"""
groupby - agrupando valores
para funcionar corretamente, os valores precisam estar ordenados
o groupby retorna um iterador
"""

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Marcos', 'nota': 'A'},
    {'nome': 'Fernando', 'nota': 'B'},
    {'nome': 'José', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'Leandro', 'nota': 'A'},
    {'nome': 'Leonardo', 'nota': 'C'},
]

# exemplo de uso do groupby
letras = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
grupos = groupby(letras)

for grupo, valores in grupos:
    print(grupo)
    print(list(valores))

print('=' * 25)

# exemplo2
alunos_agrupados = sorted(alunos, key=lambda x: x['nota'])  # ordena a lista pela nota

for aluno in alunos_agrupados:
    print(aluno)

print("=" * 25)

grupos = groupby(alunos_agrupados, key=lambda x: x['nota'])  # agrupa os alunos pela nota

for grupo, valores in grupos:
    print(grupo)

    for aluno in valores:
        print(aluno['nome'], end=', ')

    print("")
