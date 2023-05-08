"""
dicionários e **kwargs
os kwargs são argumentos nomeados, podemos passar quantos argumentos quisermos
"""


def lista_idades(**kwargs):
	lista = kwargs  # por serem keyword arguments, eles são transformados em dicionários
	print(lista)


lista_idades(João=12, Marcos=23, Leo=122)
