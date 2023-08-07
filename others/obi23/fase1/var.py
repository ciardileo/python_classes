"""
problema1 - var
"""

x, y = int(input()), int(input())  # input das coordenadas

if -9 < x < 9 and -1 < y < 9:  # verifica se esta dentro
    print("S")
else:  # verifica se a bola pegou fora da quadra
    print("N")
