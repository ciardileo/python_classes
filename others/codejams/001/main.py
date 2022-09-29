# code jam 1

def numeroParaBinario(x):
	...


def binarioParaNumero(x):
	x02 = 0  # contador de expoente
	x03 = list()  # list

	for x04 in x[::-1]:
		x03.append(int(x04) * 2 ** x02)  # adiciona o valor da formula na lista que formará o valor convertido
		x02 += 1  # soma do counter

	

def numeroParaHexadecimal(x):
	...


def hexadecimalParaNumero(x):
	...


# menu de opções
print("Convertor de binário/hexadecimal")
print("=" * 30)
print("1 - Número para binário")
print("2 - Binario para número")
print("3 - Número para hexadecimal")
print("4 - Hexadecimal para número")
print("=" * 30)

# input do usuário
x00 = int(input("Qual opção você escolhe: "))  # input opção

x01 = input('Que valor você quer converter: ')  # input valor

if x00 == 1:
	numeroParaBinario(x01)
elif x00 == 2:
	binarioParaNumero(x01)
elif x00 == 3:
	numeroParaHexadecimal(x01)
elif x00 == 4:
	hexadecimalParaNumero(x01)
