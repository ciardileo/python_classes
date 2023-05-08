# Desafio 1

def saudation(message="Boa semana", name="pessoa"):
	print(message, name)


saudation("Seja bem vindo", "Ricardo")


# Desafio 2

def soma(num1=0, num2=0, num3=0):
	print(num1 + num2 + num3)


soma(10, 22, 15)


# Desafio 3

def soma_percent(num=0, percent=0):
	return num + (num * (percent / 100))


num1, num2 = float(input("Digite um número: ")), int(input("Digite outro número: "))
a = soma_percent(num1, num2)
print(f"{a:.2f}")


# Desafio 4

def fizz_buzz(num: int):
	if num % 5 == 0 and num % 3 == 0:
		return "fizzbuzz"
	elif num % 3 == 0:
		return "fizz"
	elif num % 5 == 0:
		return "buzz"
	else:
		return num


num = int(input("Digite um número: "))
a = fizz_buzz(num)
print(a)
