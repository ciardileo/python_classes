# desafio 1
try:
    num = int(input("Digite um número inteiro: "))
    
    if num % 2 == 0:
        print("Este número é par")
    else:
        print("Este número é impar")
except:
    print("Erro, digite um número inteiro")
    

# desafio 2

try:
    hora = int(input("Que horas são (apenas a HORA)? "))

    if 0 <= hora < 5:
        print("Boa madrugada")
    elif 5 <= hora < 11:
        print("Bom dia")
    elif 11 <= hora < 18:
        print("Boa tarde")
    elif 18 <= hora <= 23:
        print("Boa noite")
    elif hora == 24:
        print(r"Para representar \"meia noite\", escreva \"0\"")
    elif hora > 24:
        print("Este horário não existe")
except:
    print("Isso não é um número")
 


# desafio 3
nome = input("Qual é seu nome?")

if nome.isnumeric():
    print("Isso não é um número")
elif len(nome) <= 4:
    print("Seu nome é curto")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")