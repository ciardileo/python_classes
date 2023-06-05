"""
exercício 161
"""


def soma(x, y):
	return x + y


def multiplica(x, y):
	return x * y


def criar_funcao(funcao, x):  # isso é chamado de closure, quando uma função é "adiada" guardando os primeiros parâmetros
	def interna(y):
		return funcao(x, y)
	return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_10 = criar_funcao(multiplica, 10)

print(soma_com_cinco(2))
print(multiplica_por_10(324))

