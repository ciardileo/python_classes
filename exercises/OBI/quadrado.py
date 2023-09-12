"""
um quadrado mágico é uma matriz n x n inteiros, em que todas as linhas, colunas e diagonais tem a mesma soma
"""


def verifica_linhas_colunas():
	soma_atual = 0
	soma = 0
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
	soma1 = 0
	soma2 = 0
	for linha in quadrado:
		soma1 += linha[quadrado.index(linha)]
		soma2 += linha[-1 - quadrado.index(linha)]

	if soma1 == soma2:
		return soma1

	return -1


n = int(input())
quadrado = []

for i in range(n):
	quadrado.append([int(x) for x in input().split()])

soma_diagonais = verifica_diagonais()
soma_linhas_colunas = verifica_linhas_colunas()

if soma_diagonais == soma_linhas_colunas and soma_diagonais != -1:
	print(soma_diagonais)
else:
	print("-1")
