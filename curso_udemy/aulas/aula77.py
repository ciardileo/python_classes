"""
count (itertools) - countador iterador sem fim
args:
start
step
"""

from itertools import count

contador = count()

for valor in contador:
	print(valor)

	if valor == 69420:
		break

# ==============================

contador = count(start=10, step=10)  # alguns parâmetros

for valor in contador:
	print(valor)

	if valor == 1000000:
		print("parando")
		break
