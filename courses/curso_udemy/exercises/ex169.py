"""
exercício: unir duas listas na ordem
pegar a menor lista como referência
"""

lista1 = ["Leo", "João", "Júlia", "Renato", "Matheus"]
lista2 = [15, 16, 17, 18, 19, 20]

lista3 = [(x, lista2[lista1.index(x)]) for x in lista1]
print(lista3)


# =========================================
# versao com função

def zipper(l1, l2):
	menor = min(len(l1), len(l2))

	return [
		(l1[i], l2[i]) for i in range(menor)
	]


print(zipper(lista1, lista2))


# ===============================
# versao com função built-in

print(list(zip(lista1, lista2)))