"""
groupby - itertools
os dados precisam estar ordenados
"""

from itertools import groupby

alunos = [
	{"nome": "Luiz", "nota": "A"},
	{"nome": "Letícia", "nota": "D"},
	{"nome": "Fabrício", "nota": "C"},
	{"nome": "Rose", "nota": "A"},
	{"nome": "Joana", "nota": "B"},
	{"nome": "João", "nota": "F"},
	{"nome": "Eduardo", "nota": "D"},
	{"nome": "André", "nota": "C"},
]

alunos.sort(key=lambda item: item['nota'])

for aluno in alunos:
	print(aluno)

alunos_agrupados = groupby(alunos, lambda item: item["nota"])

for agrupamento, valores_agrupados in alunos_agrupados:
	print(f'Agrupamento: {agrupamento}')
	for aluno in valores_agrupados:
		print(aluno)
