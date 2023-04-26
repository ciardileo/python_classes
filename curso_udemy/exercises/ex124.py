# jogo de perguntas e respostas com dicionários

from time import sleep

# lista de dicionários que guarda as perguntas do jogo
perguntas = [
	{
		'Pergunta': "Quanto é 10 x 10",
		'Opções': ["100", "120", "30", "40"],
		'Resposta': '100'
	},
	{
		'Pergunta': "Quanto é 10 / 2",
		'Opções': ["100", "120", "30", "5"],
		'Resposta': '5'
	},
	{
		'Pergunta': "Quanto é 12 x 12",
		'Opções': ["100", "144", "30", "40"],
		'Resposta': '144'
	},
]

# inicialização do programa
print("BEM VINDO AO JOGO DE PERGUNTAS")
print('='*25)
sleep(2)

# mostra as perguntas na tela
acertos = 0
for pergunta in perguntas:
	print(f"\n Pergunta: {pergunta['Pergunta']}\n")

	# printa as alternativas
	for opcao in pergunta['Opções']:
		print(f'{pergunta["Opções"].index(opcao)}) {opcao}')

	escolha = int(input("Escolha uma alternativa: "))

	# checa se o usuário acertou
	if pergunta["Opções"][escolha] == pergunta["Resposta"]:
		print("Parabéns, você acertou a pergunta!")
		acertos += 1
	else:
		print(f"Putz! Você errou a questão, a resposta certa era {pergunta['Resposta']}")

	sleep(2)

# final do jogo
print('=' * 25)
print("Calculando resultado...")
sleep(2)
print(f"FIM DE JOGO! Você acertou {acertos} de {len(perguntas)}")


