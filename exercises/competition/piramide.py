dimensao_piramide = int(input())
for i in range(1, dimensao_piramide+1):
	for j in range(1, dimensao_piramide + 1):
		print(min([i - 1, j - 1, dimensao_piramide - i, dimensao_piramide - j]) + 1, end=' ')
	print("")

# piramide = []
#
# for linha in range(1, dimensao_piramide + 1):
# 	colunas = []
# 	for coluna in range(1, dimensao_piramide + 1):
# 		colunas.append(0)
# 	piramide.append(colunas)
#
# l = 0
# for linha in piramide:
# 	c = 0
# 	for coluna in linha:
# 		teste = []
# 		numero1 = piramide.index(linha) - piramide.index(piramide[0])
# 		numero2 = piramide.index(piramide[-1]) - piramide.index(linha)
# 		numero3 = linha.index(coluna) - linha.index(linha[0])
# 		numero4 = linha.index(linha[-1]) - linha.index(coluna)
#
# 		teste.extend([numero1, numero2, numero3, numero4])
# 		print(piramide.index(piramide[2]))
# 		print(piramide.index(linha), linha.index(coluna))
# 		print(teste)
# 		print("="*25)
#
#
# 		piramide[l][c] = min(teste) + 1
# 		c += 1
# 	l += 1
#
# for linha in piramide:
# 	print(*linha)
