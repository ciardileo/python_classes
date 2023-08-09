"""
exercício - classes
"""


class Carro:
	def __init__(self, nome, fabricante, motor):
		self.nome = nome
		self.motor = motor
		self.fabricante = fabricante

	def informacoes(self):
		return f"Nome: {self.nome}\nFabricante: {self.fabricante.nome}\nMotor: {self.motor.nome}"


class Motor:
	def __init__(self, nome):
		self.nome = nome


class Fabricante:
	def __init__(self, nome):
		self.nome = nome


motor_v8 = Motor("V8")
ford = Fabricante("Ford")

mustang = Carro("Mustang", ford, motor_v8)
print(mustang.informacoes())
