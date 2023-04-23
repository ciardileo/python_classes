# exercício básico de funções
# 1: crie uma função que multiplica todos os argumentos não nomeados recebidos e retorna o total para uma variável
# 2: crie uma função que fala se um número é par ou impar

def multiplica_tudo(*numeros):
	total = 1
	for numero in numeros:
		total *= numero

	return f"O total foi: {total}"


print(multiplica_tudo(1, 4, 2, 4, 2, 89, 0))


# =====================================

def par_ou_impar(num):
	if num % 2 == 0:
		return f"{num} é par"
	return f"{num} é impar"


print(par_ou_impar(127))
