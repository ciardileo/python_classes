lista_numeros = list()
for i in range(0, 10):
	lista_numeros.append(int(input(f"{i + 1} | Escreva um número: ")))

print("=" * 25)


def verificar(lista):
	l1 = list()
	for num in lista:
		if num in l1:
			print(f"{num}: É repetido...encerrando")
			return num
		else:
			print(f"{num}: Não é repetido")
			l1.append(num)
	print("Não há nenhum número repetido na lista")
	return -1


vr = verificar(lista_numeros)
