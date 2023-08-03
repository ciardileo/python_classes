"""
exercício: carregar os dados
"""

import json

# passando os dados JSON para um dict
with open("dados.json", "r", encoding="utf8") as file:
	dados = json.load(file)


class Pessoa:
	...


pessoa1 = Pessoa()
pessoa1.__dict__ = dados
print(pessoa1.nome, pessoa1.idade, pessoa1.altura, pessoa1.cor, pessoa1.solteiro, sep=", ")