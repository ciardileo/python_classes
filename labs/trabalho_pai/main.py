"""
projeto sobre classes para a faculdade do meu pai
deve abordar os temas:
classes concretas e abstratas, métodos comuns e estáticos, herança, polimorfismo, interfaces, encapsulamento, coleção
o projeto é como uma calculadora física de movimentos
"""


# interface inicial


# classe principal (movimento retilíneo uniforme)
class MRU:
	# atributos da classe
	def __init__(self, v0=0, x0=0, t=None):
		self.velocidade_inicial = v0
		self.posicao_inicial = x0
		self.tempo = t

	@staticmethod  # método estático
	def manual():
		texto = 'Este é um simulador de MRU em Python' \
		        'Para começar, você deverá passar alguns parâmetros:' \
		        'v0 = velocidade incial do objeto' \
		        'x0 = posição inicial do objeto' \
		        't = intervalo de tempo do movimento'

		print(texto)


# classe filha (movimento retilíneo uniformimente variado)
class MRUV(MRU):
	def __init__(self, v0=0, x0=0, t=None, a=0):
		super().__init__(v0, x0, t)  # traz os atributos da classe herdada
		self.aceleracao = a

	@staticmethod  # método estático
	def manual():
		texto = 'Este é um simulador de MRUV em Python' \
		        'Para começar, você deverá passar alguns parâmetros:' \
		        'v0 = velocidade incial do objeto' \
		        'x0 = posição inicial do objeto' \
		        't = intervalo de tempo do movimento' \
		        'a = aceleração do objeto'

		print(texto)





