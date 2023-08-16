"""

"""
from itertools import zip_longest

caracteres1 = int(input())
palavra1 = input()

caracteres2 = int(input())
palavra2 = input()

ultimo_prefixo = str()
if caracteres2 > caracteres1:
    for i in range(0, caracteres1):
        if palavra1[i] == palavra2[i]:
            ultimo_prefixo += palavra1[i]
        else:
            break
else:
    for i in range(0, caracteres2):
        if palavra1[i] == palavra2[i]:
            ultimo_prefixo += palavra2[i]
        else:
            break


print(len(ultimo_prefixo))
