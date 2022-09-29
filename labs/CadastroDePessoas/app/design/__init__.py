# cria uma linha

def linha(tam=46):
    print('-' * tam)


# cria um cabeçalho

def cabecalho(txt: str):
    linha()
    print(txt.center(46))
    linha()


# cria um menu

def menu(opcs):
    count = 1
    for opc in opcs:
        print(f'\033[34m{count} - \033[m\033[36m{opc}\033[m')
        count += 1

