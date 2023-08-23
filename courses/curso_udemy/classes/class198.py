"""
classes em Python
classes são moldes que criam novos objetos (instâncias),
toda classe possui métodos (funções) e atributos (dados)
classes utilizam o PascalCase

programação orientada a objetos possui 4 pilares:
	- abstração: classes abstratas (abc) são classes que só existem para serem herdadas e não podem ser utilizadas sozinhas
	- herança: herdar classes para especializá-las
	- encapsulamento: public, protected, private
	- polimorfismo: quando dois métodos de uma classe abstrata possuem a mesma assinatura mas funções diferentes
"""


class Pessoa:
	# o __init__ é o método que INICIALIZA OS ATRIBUTOS da classe
	def __init__(self, nome, sobrenome):  # o self é um parâmetro reservado que referencia a instância da classe
		self.nome = nome
		self.sobrenome = sobrenome


pessoa1 = Pessoa("Leo", "Ciardi")  # pessoa1 é uma instância de Pessoa, ele que é referenciado pelo self
print(pessoa1.nome, pessoa1.sobrenome)

print(pessoa1.__init__("leo", "ciardi"))  # o método __init__ sempre retorna None
