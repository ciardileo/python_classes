"""
*args e **kwargs em python (só basta o asterisco, não é necesário escrever "args")
os args são dados em tuplas
os kwargs são dados em dicionários e devem ser declarados com {chave}={valor}
"""


def func(*argumentos, **key_word_arguments):
	print(argumentos, )
	print(key_word_arguments)


func(1, 23, 34, nome="Leo", idade="14")

list1 = [1, 2, 3, 4, 5]
num1, num2, *nums = list1  # o asterisco indica que ele receberá todos os valores até o final, é usado em funções para passar muitos parametros

print(*list1)  # printa a lista desempacotada, como se fosse valores separados
