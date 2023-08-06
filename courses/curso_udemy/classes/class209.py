"""
métodos de classe (@classmethods)
métodos de classe são métodos que não precisam de uma instância como parâmetro para ser executado,
então podem ser chamados apenas com Classe.metodo()
para ser um método de classe, devemos colocar o decorador @classmethod antes da função e passar cls como parâmetro
eles são comumente usados para criar factories, métodos que criam novos objetos

métodos estáticos (@staticmethods)
eles não tem muita utilidade, só servem como uma organização do código, para a função estar dentro da função
porém, esse método não tem acesso nem ao self, nem ao cls, portanto é uma função normal
"""


class Pessoa:
	ano_atual = 2023

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	# exemplo de um classmethod que cria um factory method (gera novas instâncias)
	@classmethod
	def metodo_de_classe(cls, nome):
		return cls(nome, 50)  # vai retornar uma instância de Pessoa

	@staticmethod
	def metodo_estatico():
		print("Minha única função é organizar")
