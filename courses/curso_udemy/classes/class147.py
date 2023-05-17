"""
generator functions
"""


def generator(n=0):
	yield 1  # pausa
	print("Continuando...")
	yield 2
	print("Mais uma vez...")
	yield 4
	print("Vou terminar...")
	return "Acabou"


gen = generator(0)
print(next(gen))
print(next(gen))
print(next(gen))
