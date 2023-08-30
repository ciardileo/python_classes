"""
métodos em classes Python
o self é apenas uma convenção, podemos utilizar qualquer nome, ele só precisa ser o primeiro argumento para ter sua função

atributos de classe
atributos de classe são variáveis que são definidas para todo o molde da classe, fora do __init__
eles não podem ser chamados com self.var

__dict__
retorna todas os atributos da classe em um dicionário
"""


class Carro:
	# atributos de classe

	ano_atual = 2023

	def __init__(self, nome, marca, cor, ano):
		self.nome = nome
		self.marca = marca
		self.cor = cor
		self.ano = ano

	def acelerar(self):  # método dentro da classe
		print(f"{self.nome} acelerou!")

	def idade(self):
		print(f"seu carro tem {self.ano_atual - self.ano} anos de idade")


camaro = Carro("camaro", "chevrolet", cor="amarelo", ano=2010)  # podemos usar kwargs
camaro.acelerar()
camaro.idade()

print(camaro.__dict__)  # função que retorna todos os atributos da classe em formato de dicionário
# print(vars(camaro)) mesma função
