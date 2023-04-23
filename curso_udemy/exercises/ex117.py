# exercício de funções da aula 117
# crie funções que duplicam, triplicam e quadruplicam o número recebido

def cria_funcao(fator=2):
	def incremento(numero=1):
		return numero * fator

	return incremento


fator_multiplicativo = int(input("Digite o fator multiplicativo: "))
numero_multiplicado = float(input("Digite o número a ser multiplicado: "))

funcao = cria_funcao(fator_multiplicativo)
print(funcao(numero_multiplicado))
