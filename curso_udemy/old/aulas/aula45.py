# operadores ternários em python

answer = input("Deseja logar na sua conta? [s/n]: ")

logged_user = True if answer == "s" else False  # funciona como um list comprehension, é uma forma reduzida para um if

mensagem = "Logado" if logged_user else "Deslogado"

print(mensagem)

##########################################################

idade = int(input("Qual é sua idade?: "))
maioridade = (idade >= 18)  # colocamos uma condição entre parênteses para atribuir rapidamente um valor booleano a uma variável

mensagem = "Maior de 18 anos" if maioridade else "Menor de 18 anos"
print(mensagem)


