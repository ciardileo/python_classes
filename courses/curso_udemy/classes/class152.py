"""
raise - como criar erros próprios
"""


def divide(n, d):
	try:
		return n / d
	except ZeroDivisionError:
		print("Deu o seguinte erro:")
		raise


print(divide(10, 0))

raise ValueError("Erro desconhecido!")
