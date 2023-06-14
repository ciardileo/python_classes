"""
problema3 - subsequência
"""

# lista das duas sequências
sequencia_a = list()
sequencia_b = list()
sequencia2 = list()

tamA = int(input())
tamB = int(input())

for i in range(0, tamA):
    item = int(input())
    sequencia_a.append(item)

for i in range(0, tamB):
    item = int(input())
    sequencia_b.append(item)

maior = 0
cont = 0

for i in range(min(sequencia_a), max(sequencia_a) + 1):
    sequencia2.append(i)

pertence = True
for i in sequencia_b:
    if sequencia2.index(i) == -1:
        pertence = False

if pertence:
    numero = sequencia_b[0]
    for i in sequencia_b:
        if i < numero:
            print("N")
        else:
            numero = i
    if numero == sequencia_b[-1]:
        print("S")
else:
    print("N")