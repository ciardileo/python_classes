"""
projeto sobre classes para a faculdade do meu pai
deve abordar os temas:
classes concretas e abstratas, métodos comuns e estáticos, herança, polimorfismo, interfaces, encapsulamento, coleção
o projeto é como uma calculadora física de movimentos
"""

# função importada que dá uma pausa no código
from time import sleep


# classe principal (movimento retilíneo uniforme)
class MRU:
	# atributos da classe
	def __init__(self, v0=0, x0=0, t=None):
		self.velocidade_inicial = v0
		self.posicao_inicial = x0
		self.tempo = t

	# função que mostra um manual das variáveis
	@staticmethod  # método estático
	def manual():
		texto = 'Explicação das variáveis do estudo do movimento:\n' \
		        'v0 = velocidade incial do objeto (m/s)\n' \
		        'x0 = posição inicial do objeto (m)\n' \
		        't = intervalo de tempo do movimento (s)\n' \
		        'a = aceleração do objeto (m/s²)\n'

		print("=-" * 25)
		print(texto)
		print("=-" * 25)

	# função para redefinir os valores das variáveis
	def variaveis(self):
		while True:
			try:
				print('=-' * 25)
				print("Defina as variáveis abaixo 👇🏻")
				sleep(1)
				self.velocidade_inicial = float(input("Velocidade inicial (em m/s): "))
				self.posicao_inicial = float(input("Posição inicial (em metros): "))
				self.tempo = float(input("Intervalo de tempo (em segundos): "))
				print('=-' * 25)

				break
			except:
				print("ERRO! DIGITE NOVAMENTE!")

	# função que calcula a posição final conforme a equação de MRU
	def posicao_final(self):
		pos = self.posicao_inicial + self.velocidade_inicial * self.tempo
		print("=-" * 25)
		print(
			f"Com uma velocidade de {self.velocidade_inicial} m/s, o objeto sairá da posição {self.posicao_inicial} para a {pos} em {self.tempo} segundos.")
		print("=-" * 25)


# classe filha (movimento retilíneo uniformimente variado)
class MRUV(MRU):
	def __init__(self, v0=0, x0=0, t=None, a=0):
		super().__init__(v0, x0, t)  # traz os atributos da classe herdada
		self.aceleracao = a

	# função que redefine as variáveis
	def variaveis(self):
		while True:
			try:
				print('=-' * 25)
				print("Defina as variáveis abaixo 👇🏻")
				sleep(1)
				self.velocidade_inicial = float(input("Velocidade inicial (em m/s): "))
				self.posicao_inicial = float(input("Posição inicial (em metros): "))
				self.tempo = float(input("Intervalo de tempo (em segundos): "))
				self.aceleracao = float(input("Aceleração (em m/s²): "))
				print('=-' * 25)

				break
			except:
				print("ERRO! DIGITE NOVAMENTE!")

	# função que calcula a posição final com base na equação de MRUV
	def posicao_final(self):  # exemplo de polimorfismo
		pos = self.posicao_inicial + (self.velocidade_inicial * self.tempo) + ((self.aceleracao * self.tempo ** 2) / 2)
		print("=-" * 25)
		print(
			f"Com uma velocidade de {self.velocidade_inicial} m/s e aceleração de {self.aceleracao} m/s², o objeto sairá da posição {self.posicao_inicial} para {pos} em {self.tempo} segundos.")
		print("=-" * 25)

	# função que calcula a velocidade final com base na equação horária da velocidade
	def velocidade_final(self):
		vel = self.velocidade_inicial + self.aceleracao * self.tempo
		print("=-" * 25)
		print(f"A velocidade final será {vel} m/s")
		print("=-" * 25)


# interface
print("Ferramenta de Estudo do Movimento")
print('=-' * 25)

while True:
	try:
		print(
			"Digite 1 para calcular MRU (sem aceleração)\nDigite 2 para calcular MRUV (com aceleração)\nDigite 3 para sair")
		tipo = int(input('Qual opção você quer: '))
		if tipo == 1:
			mru = MRU()
			mru.variaveis()

			while True:
				try:
					sleep(2)
					print(
						"MENU:\nDigite 1 para redefinir as variáveis\nDigite 2 para mostrar o manual\nDigite 3 para calcular a posição final\nDigite 4 para sair")
					sleep(2)

					opc = int(input("Qual opção você deseja: "))
					if opc == 1:
						mru.variaveis()
					elif opc == 2:
						mru.manual()
					elif opc == 3:
						mru.posicao_final()
					elif opc == 4:
						print("Saindo...")
						sleep(2)
						break
					else:
						print("ERRO! ESTA OPÇÃO NÃO EXISTE")
				except:
					print('ERRO! DIGITE UM NÚMERO VÁLIDO')
		elif tipo == 2:
			mruv = MRUV()
			mruv.variaveis()

			while True:
				try:
					sleep(2)
					print(
						"MENU:\nDigite 1 para redefinir as variáveis\nDigite 2 para mostrar o manual\nDigite 3 para calcular a posição final\nDigite 4 para calcular a velocidade final\nDigite 5 para sair")
					sleep(2)

					opc = int(input("Qual opção você deseja: "))
					if opc == 1:
						mruv.variaveis()
					elif opc == 2:
						mruv.manual()
					elif opc == 3:
						mruv.posicao_final()
					elif opc == 4:
						mruv.velocidade_final()
					elif opc == 5:
						print("Saindo...")
						sleep(2)
						break
					else:
						print("ERRO! ESTA OPÇÃO NÃO EXISTE")
				except:
					print('ERRO! DIGITE UM NÚMERO VÁLIDO')

		elif tipo == 3:
			print("Saindo do programa!")
			break
		else:
			print("ERRO! DIGITE UMA OPÇÃO VÁLIDA")
	except:
		print("ERRO! DIGITE UM NÚMERO!")
	finally:
		print('=-' * 25)
		print("Reiniciando...")
		print('=-' * 25)
