"""
um quadrado mágico é uma matriz n x n inteiros, em que todas as linhas, colunas e diagonais tem a mesma soma
"""


def verifica_linhas_colunas():
	soma_atual = 0
	for linha in quadrado:
		# soma da linha
		soma = sum(linha)

		# soma da coluna
		for coluna in linha:
			for j in range(len(quadrado)):
				soma_atual += quadrado[j][linha.index(coluna)]
			if soma_atual == soma:
				soma_atual = 0
			else:
				return -1

		return soma


def verifica_diagonais():
	...


n = int(input())
quadrado = []

for i in range(n):
	quadrado.append([int(x) for x in input().split()])

print(verifica_linhas_colunas())
