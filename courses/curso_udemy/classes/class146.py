"""
generators, iterators and iterables
generators economizam MUITO mais memória do que iteráveis, já que geradores não salva todos na memória
o problema com os geradores é que não podemos acessar qualquer item, só seguir a ordem
"""

iteravel = ['Eu', 'Tenho', '__iter__']  # exemplo de iterável
iterador = iter(iteravel)  # criação de um iterador com a função iter(), é como um for

lista = [n for n in range(100)]
gerador = (n for n in range(100))  # generator expression, criada com os parênteses

print(lista)
print(gerador)

for item in gerador:
	print(item)
