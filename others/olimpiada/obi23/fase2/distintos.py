"""

"""

maior_intervalo = 0
sequencia = list()
sequencia_atual = list()

n = int(input())

for i in range(0, n):
    sequencia.append(int(input()))

# print(sequencia)

for num in sequencia:
    # print(sequencia_atual, num)
    if num not in sequencia_atual:
        sequencia_atual.append(num)
        if len(sequencia_atual) > maior_intervalo:
            maior_intervalo = len(sequencia_atual)

        # print(sequencia_atual, maior_intervalo)
    else:
        # print("passei aqui")
        for num2 in sequencia_atual:
            if num2 == num:
                for i in range(0, sequencia_atual.index(num2) + 1):
                    try:
                        del sequencia_atual[i]
                    except:
                        pass
                break


        sequencia_atual.append(num)

    # print("---")



print(maior_intervalo)
