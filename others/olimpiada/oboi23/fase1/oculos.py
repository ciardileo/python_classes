"""
N oculos enfileirados - numerados de 1 a N
o óculos i tem grau esquerdo e e direito d
enzo precisa de E e D
a pontuação do óculos é | e - E | + | d - D |
quanto menor a pontuação, melhor é o oculos
"""

# quantidade de oculos, grau de enzo
N, E, D = list(map(int, input().split()))

oculos = list()

for i in range(1, N + 1):
	e, d = list(map(int, input().split()))

	pontuacao = abs(e - E) + abs(d - D)

	oculos.append([e, d, pontuacao])


oculos.sort(key=lambda x: x[2])
print(oculos[0][2])
