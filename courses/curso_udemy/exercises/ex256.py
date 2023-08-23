"""
exercício envolvendo os conceitos de abstração, herança, polimorfismo e encapsulamento em python
criar um sistema bancário
"""

from abc import ABC, abstractmethod


class Conta(ABC):  # classe abstrata
	def __init__(self, banco, agencia, numero_conta, saldo):
		self.banco = banco
		self.agencia = agencia
		self.numero_conta = numero_conta
		self.saldo = saldo

	@abstractmethod
	def sacar(self, quantia): ...  # método abstrato que vai ser definido pelas subclasses

	def deposito(self, quantia):
		print(f"Depositei R${quantia} na conta {self.numero_conta}")
		self.saldo += quantia


class ContaCorrente(Conta):
	def sacar(self, quantia):
		if self.banco.autenticar():
			self.saldo -= quantia
			print(f"Sacou R${quantia}\nPatrimônio atual: {self.saldo}")


class ContaPoupanca(Conta):
	def sacar(self, quantia):  # a função sacar é um polimorfismo com a da classe ContaCorrente
		if self.banco.autenticar():
			if self.banco.autenticar():
				if quantia > self.saldo:
					self.saldo -= quantia - self.saldo
					print(f"Sacou R${quantia}\nPatrimônio atual: {self.saldo}")
				else:
					self.saldo -= quantia
					print(f"Sacou R${quantia}\nPatrimônio atual: {self.saldo}")


class Pessoa(ABC):  # classe abstrata
	def __init__(self, nome, idade):
		self._nome = nome  # atributos protegidos
		self._idade = idade

	@property
	def idade(self):
		return self._idade

	@idade.setter
	def idade(self, valor):
		self._idade = valor

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, valor):
		self._nome = valor


class Cliente(Pessoa):
	def __init__(self, nome, idade, conta):
		super().__init__(nome, idade)
		self.conta = conta
		self.registrar_conta()

	def registrar_conta(self):
		if self.conta.agencia in self.conta.banco.agencias:
			self.conta.banco.clientes += self
		else:
			print(f"A agência {self.conta.agencia} não existe no banco")


class Banco:
	def __init__(self):
		self.agencias = []
		self.clientes = []

	def autenticar(self, cliente: Cliente):
		if cliente in self.clientes:
			return True
		return False

	def adicionar_agencia(self, *agencias):
		self.agencias += agencias


# =============================================================================================

nubank = Banco()
nubank.adicionar_agencia(1, 2)

inter = Banco()
inter.adicionar_agencia(3, 4)

leo = Cliente("Leo", 15, ContaCorrente(nubank, 1, 10, 300))
marcos = Cliente("Marocos", 20, ContaPoupanca(inter, 3, 11, 500))

leo.conta.deposito(600)
leo.conta.sacar(2000)