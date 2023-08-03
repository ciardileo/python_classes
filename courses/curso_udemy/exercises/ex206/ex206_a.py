"""
exercício: salvar e carregar os atributos de uma instância de uma classe em outra
"""

import json


class Pessoa:
	def __init__(self, nome, idade, cor, altura, solteiro):
		self.nome = nome
		self.idade = idade
		self.cor = cor
		self.altura = altura
		self.solteiro = solteiro


# instância da classe
pessoa1 = Pessoa("Leo", 15, "branco", 1.76, False)

# salvando os atributos em JSON
with open("dados.json", "w", encoding="utf8") as file:
	json.dump(pessoa1.__dict__, file, indent=2)
