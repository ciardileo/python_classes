"""
Validador de CPF
"""

cpf = input("Digite um cpf para validação: ")

numlist1, numlist2 = list(), list()

for indice, mult in enumerate(range(10, 1, -1), 0):
	numlist1.append(mult * int(cpf[indice]))

digit1 = 11 - (sum(numlist1) % 11)
digit1 = digit1 if digit1 <= 9 else 0

for indice, mult in enumerate(range(11, 1, -1), 0):
	if mult == 2:
		numlist2.append(mult * digit1)
	numlist2.append(mult * int(cpf[indice]))

digit2 = 11 - (sum(numlist2) % 11)
digit2 = digit2 if digit2 <= 9 else 0

print(f"Os dois dígitos finais são {digit1} e {digit2}")

is_a_sequence = cpf == cpf[0] * len(cpf)

if int(cpf[-1]) is digit2 and int(cpf[-2]) is digit1 and not is_a_sequence:
	print("CPF Válido")
else:
	print(f"CPF Inválido, segundo os primeiros 9 números, os útlimos dois deveriam ser {digit1} e {digit2}")