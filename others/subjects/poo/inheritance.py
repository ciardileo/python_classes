# class
class Carro:
	def __init__(self, marca: str, ano: int, tipo: str):
		# método construtor/consultor
		self.marca = marca
		self.ano = ano
		self.tipo = tipo

	def abastecer(self):
		print(f'Abastecemos o seu carro, por ser {self.tipo}, você pagará 10 reais a mais')

	def consertar(self):
		print(f'Seu carro de {self.ano} foi consertado, por ser desse ano, você pagará R$ {self.ano / 10:.2f}')


meu_carro = Carro('Chevrolet', 2013, 'Sedan')
meu_carro.consertar()
