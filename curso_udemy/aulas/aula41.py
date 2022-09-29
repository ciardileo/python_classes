lista = ["aaa", "232", "a2", "b23"]
print(lista)

for indice, valor in enumerate(lista, 21):  # podemos indicar em qual número o índice começa
	print(f"[{indice}] {valor}")

# o enumerate() retorna um iterator

