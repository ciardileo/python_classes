"""
exercícios sobre tratamento de erros
"""

# exercício 1
while True:
	try:
		num1 = float(input("Digite um número: "))
		num2 = float(input("Digite outro número: "))
		print(f"A divisão entre {num1} e {num2} é {num1/num2}")
		break
	except (TypeError, ValueError):
		print("ERRO! POR FAVOR, ESCREVA UM NÚMERO VÁLIDO")
	except ZeroDivisionError:
		print("ERRO! NÃO É POSSÍVEL DIVIDIR POR ZERO")

# exercício 2
while True:
	try:
		nome_arquivo = input("Nome do arquivo: ")
		arquivo = open(nome_arquivo, 'r+')

		linhas = arquivo.readlines()
		for linha in linhas:
			print(linha)

		arquivo.close()
		break
	except (TypeError, ValueError):
		print("ERRO! Digite um arquivo válido!")
	except FileNotFoundError:
		print("ERRO! Este arquivo não existe!")

# exercício 3
while True:
	try:
		numero = float(input("Digite um número entre 1 e 10: "))

		if numero < 1 or numero > 10:
			print("ERRO! Número fora dos limites!")
		else:
			break

	except (TypeError, ValueError):
		print("ERRO! DIGITE UM NÚMERO VÁLIDO")

