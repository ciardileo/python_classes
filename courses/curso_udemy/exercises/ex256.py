"""
exercício envolvendo os conceitos de abstração, herança, polimorfismo e encapsulamento em python
criar um sistema bancário
"""

from abc import ABC, abstractmethod
import time
from rich import print
from rich.console import Console
import os


class Conta(ABC):  # classe abstrata
	def __init__(self, agencia, numero_conta, saldo):
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
		self.saldo -= quantia
		print(f"Sacou R${quantia}\nPatrimônio atual: R${self.saldo}")


class ContaPoupanca(Conta):
	def sacar(self, quantia):  # a função sacar é um polimorfismo com a da classe ContaCorrente
		if quantia > self.saldo:
			self.saldo -= quantia - self.saldo
		else:
			self.saldo -= quantia

		print(f"Sacou R${quantia}\nPatrimônio atual: R${self.saldo}")


class Pessoa:  # classe abstrata
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
	def __init__(self, nome, idade):
		super().__init__(nome, idade)
		self.conta = None


class Banco:
	def __init__(self):
		self.agencias = []
		self.clientes = []
		self.contas = []

	def autenticar(self, cliente: Cliente):
		if cliente in self.clientes and cliente.conta in self.contas and cliente.conta.agencia in self.agencias:
			return True

		print("Sua conta não pode ser autenticada")
		return False

	def adicionar_agencia(self, *agencias):
		self.agencias += agencias


# =============================================================================================
# interface

if __name__ == "__main__":
	print("bem vindo ao sistema bancário 1.0")
	print("=" * 25)

	console = Console()

	while True:
		opcoes = \
			"opções:\n" \
			"1 - configuração dos bancos\n" \
			"2 - configuração dos clientes\n" \
			"3 - sair"

		print(opcoes)
		print("=" * 25)

		try:
			time.sleep(1)
			escolha = int(input("digite uma opção: "))
		except ValueError:
			print("[red]ERRO! DIGITE UMA OPÇÃO VÁLIDA")
			time.sleep(1)
			os.system("cls")


