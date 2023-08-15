"""
mapa: n colunas, m linhas
linhas: oeste-leste
colunas: norte-sul
foram instaladas k cameras, que podem ser apontadas para várias posições
"""


def marcar_camera(linha, coluna, direcao):
	if direcao == "S":
		for cel in range(0, m - linha):
			mapa[linha + cel][coluna] = 1
	elif direcao == "N":
		for cel in range(0, linha + 1):
			mapa[linha - cel][coluna] = 1
	elif direcao == "L":
		for cel in range(0, n - coluna):
			mapa[linha][coluna + cel] = 1
	elif direcao == "O":
		for cel in range(0, coluna + 1):
			mapa[linha][coluna - cel] = 1


n, m, k = [int(x) for x in input().split()]

mapa = [[0] * n for x in range(1, m+1)]

for i in range(1, k + 1):
	c, l, d = [x for x in input().split()]
	marcar_camera(int(l) - 1, int(c) - 1, d)

print(*mapa, sep='\n')

if mapa[0][0] == 1:
	print("N")
else:
	for linha in mapa:
		for celula in linha:
			...


