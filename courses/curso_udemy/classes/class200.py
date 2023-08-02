"""
métodos de classes em Python
o self é apenas uma convenção, podemos utilizar qualquer nome, ele só precisa ser o primeiro argumento para ter sua função
"""


class Carro:
	def __init__(self, nome, marca, cor, ano):
		self.nome = nome
		self.marca = marca
		self.cor = cor
		self.ano = ano

	def acelerar(self):  # método dentro da classe
		print(f"{self.nome} acelerou!")


camaro = Carro("camaro", "chevrolet", cor="amarelo", ano=2010)  # podemos usar kwargs


