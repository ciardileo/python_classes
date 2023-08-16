"""
divide em grupos de 3
lista de pares que querem estar juntos
lista de pares que não querem estar juntos
"""

total_estudantes, mesmo_gp, gp_separado = [int(x) for x in input().split()]
restricoes = 0
# estudantes = [x for x in range(1, total_estudantes + 1)]



pares_juntos = list()
for i in range(0, mesmo_gp):
    x, y = [int(num) for num in input().split()]
    pares_juntos.append([x, y])

pares_separados = list()
for i in range(0, gp_separado):
    u, v = [int(num) for num in input().split()]
    pares_separados.append([u, v])


grupos = list()
for i in range(0, int(total_estudantes // 3)):
    a, j, k = [int(num) for num in input().split()]
    grupos.append([a, j, k])

for grupo in grupos:
    for separado in pares_separados:
        if separado[0] in grupo and separado[1] in grupo:
            restricoes += 1

    for junto in pares_juntos:
        if (junto[0] in grupo and junto[1] in grupo) or (junto[0] not in grupo and junto[1] not in grupo):
            pass
        else:
            pares_juntos[pares_juntos.index(junto)] = [0, 0]
            restricoes += 1


print(restricoes)