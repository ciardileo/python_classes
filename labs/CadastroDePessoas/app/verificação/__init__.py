# verifica se é um número e responde erros


def leiaopc(opc, limite=3):
    while True:
        try:
            num = int(input(opc))

            if num > limite:
                print('\033[31mERRO! Essa opção não existe!\033[m')
                continue
            elif num < 0:
                print('\033[31mERRO! As oções começam a partir do número 1\033[m')
            else:
                return num
                break
        except:
            print('\033[31mERRO! Digite um número válido!\033[m')


def leiaint(txt):
    while True:
        try:
            num = int(input(txt))

            return num
            break

        except:
            print('\033[31mERRO! Digite um número válido!\033[m')
