"""
Desafios - list comprehension
"""

# minha resolução

string = '012345678901234567890123456789012345678901234567890123456789'
lista = [s + "9" for s in string[:-1].split("9")]
print(lista)

print(".".join(lista))

# =========================================================
# resolução do professor

n = 10
comp = [string[i:i + n] for i in range(0, len(string), n)]
print(comp)
