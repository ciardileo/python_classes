"""
métodos getter e setter
================
getter é todo método usado para obter um atributo
normalmente criamos um método normal para retornar tal atributo, mas em Python podemos utilizar
o decorador @property antes do método para fazer com que ele seja chamado como um atributo

setter é todo método usado para setar o valor de um atributo
para fazer um setter no modo pythonico, utilizamos @property.setter

funções setter e getter são usadas normalmente para esconder as variáveis do código
ou para tratar casos e erros
===========================================
convenções de encapsulamento:
sem underline: atributo/método público
1 underline: atributo/método protegido, só pode ser acessado dentro da classe ou das subclasses
2 underlines: atributo/método privado, só pode ser acessado dentro da classe principal
"""


class Caneta:
	def __init__(self, cor, preco):
		self._cor = cor
		self.preco = preco

	@property  # o "@property" faz com que o método possa ser chamado sem parênteses, como um atributo
	def cor(self):
		print("get cor")
		return self._cor

	@cor.setter  # decorador que faz a o método-atributo virar um setter, capaz de ser atribúido como uma variável
	def cor(self, valor):
		print("set cor")
		self._cor = valor


caneta = Caneta("preta", 5)
caneta.cor = "vermelho"
print(caneta.cor)
