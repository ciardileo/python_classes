# Desafio 1

def func1():
	return 12


def func2():
	return func1()


a = func2()
print(a)


# Desafio 2

def bom_dia(nome):
	return f"Bom dia {nome}"


def soma(num1, num2):
	return num1 + num2


def func1(func):
	return func()


def func2():
	return soma(15, 2), bom_dia("Leo")


a = func1(func2)
print(*a, sep="\n")
