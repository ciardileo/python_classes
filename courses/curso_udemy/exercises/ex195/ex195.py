"""
exercício -> fazer um programa de lista de tarefas com função de refazer e desfazer e que salva em JSON
"""

import os
import json


# desfaz o último item
def desfazer():
	try:
		lixeira.append(lista[-1])
		print(f"\nitem {lista[-1]} desfeito")
		lista.pop()
	except IndexError:
		print("\nnada a desfazer")
	finally:
		print("")


# refaz o último item apagado
def refazer():
	try:
		lista.append(lixeira[0])
		print(f"\nitem {lixeira[0]} readicionado")
		del(lixeira[0])

	except IndexError:
		print("\nnada a refazer")
	finally:
		print("")


def salvar():
	with open(arquivo_json, "w", encoding="utf8") as arquivo:
		json.dump(lista, arquivo, indent=2)

	print("\narquivo salvo com sucesso!\n")


def carregar():
	with open(arquivo_json, "r", encoding="utf8") as arquivo:
		global lista
		lista = json.load(arquivo)

	print("\nlista carregada com sucesso\n")


# função que mostra a lista
def listar():
	print("\nITENS:")
	print(*lista, sep="\n")
	print("")


# lista principal
lista = []

# lista dos itens apagados
lixeira = []

# caminho do arquivo JSON
arquivo_json = "tarefas.json"

# interface
print("BEM-VINDO AO APLICATIVO DE TAREFAS")

while True:
	print("comandos: desfazer, refazer, listar, limpar, salvar, carregar, sair")

	# resposta do usuário
	resposta = input("digite um comando ou tarefa: ")

	if resposta == "desfazer":
		desfazer()
	elif resposta == "refazer":
		refazer()
	elif resposta == "listar":
		listar()
	elif resposta == "limpar":
		os.system("cls")
	elif resposta == "salvar":
		salvar()
	elif resposta == "carregar":
		carregar()
	elif resposta == "sair":
		print("saindo do programa...")
		break
	else:
		lista.append(resposta)
		print(f"\nitem {resposta} adicionado com sucesso\n")
