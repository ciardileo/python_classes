# largura, comprimento, jogadas
N, M, P = list(map(int, input().split()))

matriz = list()

# soma jogadores
soma_enzo = 0
soma_lobo = 0

for i in range(1, N + 1):
	valores = list(map(int, input().split()))
	matriz += [valores]

for i in range(1, P+1):
	l, c = list(map(int, input().split()))
	pontuacao = sum(matriz[l-1])

	for item in matriz[l-1]:
		matriz[l-1][matriz[l-1].index(item)] = 0

	for k in matriz:
		pontuacao += k[c-1]
		k[c-1] = 0

	if i % 2 == 0:
		soma_lobo += pontuacao
	else:
		soma_enzo += pontuacao

if soma_enzo > soma_lobo:
	print("Enzo")
elif soma_enzo < soma_lobo:
	print("Lobo")
else:
	print("Empate")





