"""
Herança x Composição
================================================
Associação - uma classe usa outra como ferramente
Agregação - uma classe faz parte de outra
Composição - uma classe só existe dentro da outra
=================================================
Herança - uma classe é outra, só que extendida, herdando suas características
Usamos herança para tornar uma classe muito específica mais genérica, podendo reutilizá-la depois

Class.mro() // Class.__mro__ => retorna a ordem de busca dos métodos em uma subclasse e suas superiores

quando chamamos uma classe herdada, ela primeiro buscará métodos dela mesmo, e se não achar, buscará nas classes acima,
logo, a classe filha tem maior prioridade de chamada

classe principal (pessoa):
	é chamada de: super class, base class, parent class
classes filhas (cliente):
	é chamada de: child class, sub class, derived class

podemos herdar mais de uma classe, a chamada herança múltipla
as heranças múltiplas podem  geram mixins, que é quando uma classe que não está na família entra por meio da herança

super()
a função super() retorna uma instância da classe pai
ela serve para quando queremos modificar o __init__ ou um método, mas ainda mantendo as funcionalidades do pai
dentro dos parênteses do super(), nós podemos passar uma classe diferente para receber a superior a ela
"""


class Pessoa:
	def __init__(self, nome, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome

	def falar(self):
		print(f"Oi, meu nome é {self.nome}")


class Cliente(Pessoa):  # entre parênteses colocamos a classe pai
	def __init__(self, nome, sobrenome, compras):
		super().__init__(nome, sobrenome)  # inicializa o __init__ da super classe com esses parâmetros
		self.total_compras = compras

	def falar(self):
		print("Eu sou um cliente")
		super().falar()  # retorna o falar() da classe pai Pessoa


p1 = Pessoa("Raí", "Ramos")
c1 = Cliente("Marcos", "Ribeiro", 26)

p1.falar()
c1.falar()
