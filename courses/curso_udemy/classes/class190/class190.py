"""
manipulação de arquivos JSON
arquivos JSON aceitam todos os tipos de dados primitivos, além de objetos (dicionários) e arrays (listas)
"""

# módulo do JSON
import json

# dicionário em formato similar ao JSON
personagem = {
	"nome": "Leo",
	"hp": 90,
	"nivel": 12.5,
	"itens": [
		{"nome": "espada_do_dragao", "nivel": 2},
		{"nome": "pocao_de_cura", "nivel": 10}
	],
	"matou_boss": True,
}

# Python => Json
with open("personagem.json", "w", encoding="utf8") as arquivo:
	# função que transforma um objeto Python em JSON
	json.dump(personagem, arquivo, ensure_ascii=False, indent=2)  # ensure_ascii decide se o arquivo será formatado em ASCII ou nao, indent=2 serve para formatar o arquivo de uma maneira mais bonita

# Json => Python
with open("personagem.json", "r", encoding="utf8") as arquivo:
	pessoa = json.load(arquivo)  # função inversa ao json.dump()
	print(pessoa)



