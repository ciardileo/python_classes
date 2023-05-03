"""
funções lambda
"""


def executa(funcao, *args):
	return funcao(args)


print(executa(lambda x, y: x + y, 2, 3))  # lambda que faz uma soma
print(executa(lambda x, y, z: x * y ** z, 2, 3, 4))  # lambda que faz uma operação

soma = lambda *args: sum(args)
print(soma(12, 23, 34, 56, 123))
