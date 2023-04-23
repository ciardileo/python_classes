nome = "Roberto"
idade = 32
altura = 1.89
peso = 81.2
ano_atual = 2022

ano_nascimento = ano_atual - idade
imc = peso * altura ** 2

print(
	f"Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}\nAno Atual: {ano_atual}\nAno de Nascimento: {ano_nascimento}\nIMC: {imc:.2f}")
