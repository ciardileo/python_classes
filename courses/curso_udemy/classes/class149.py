"""
tratamento de erros em Python
os erros são "ignorados" dentro do try
podemos executar coisas diferentes dependendo do erro
"""

try:
	a = 18
	b = 0
	c = a / b
except ZeroDivisionError:
	print("Dividiu por 0")
except (IndexError, TypeError):  # conseguimos colocar duas exceções ao mesmo tempo em uma tupla
	print("Index error e type error")
except Exception as error:  # podemos pegar a mensagem da exceção
	print("Erro desconhecido")
	print(error)
	print(error.__class__.__name__)  # nome do erro

