"""
Gerador de CPF
"""

# imports
import random

while True:
	random_cpf = str(random.randint(10000000000, 99999999999))

	numlist1, numlist2 = list(), list()

	for indice, mult in enumerate(range(10, 1, -1), 0):
		numlist1.append(mult * int(random_cpf[indice]))

	digit1 = 11 - (sum(numlist1) % 11)
	digit1 = digit1 if digit1 < 9 else 0

	for indice, mult in enumerate(range(11, 1, -1), 0):
		if mult == 2:
			numlist2.append(mult * digit1)
		numlist2.append(mult * int(random_cpf[indice]))

	digit2 = 11 - (sum(numlist2) % 11)
	digit2 = digit2 if digit2 < 9 else 0

	print(f"CPF Original: {random_cpf}\nCPF Válido: {random_cpf[:-2] + str(digit1) + str(digit2)}")

	repeat = input("Você quer gerar outro CPF? [s/n]: ")
	if repeat == 'Ss':
		continue
	else:
		break

print("\nEncerrando o programa...")
