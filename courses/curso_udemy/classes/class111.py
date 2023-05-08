"""
args - argumentos não nomeados
com o *args, conseguimos passar quantos parâmetros quisermos a uma função
"""

x, y, *resto = 1, 2, 3, 4


def soma(*args):
	total = 0
	for num in args:
		total += num
	print(total)


soma(1, 2, 3, 4, 5, 6)


# ====================================
# quando utilizamos o asterisco antes da lista/tupla, nós desempacotamos ela e enviamos seus valores como parâmetros separados

def operacao(inicial, multiplica, adiciona):
	return inicial * multiplica + adiciona


argumentos = (2, 5, 3)
print(operacao(*argumentos))
