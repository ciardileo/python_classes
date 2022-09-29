from ..design import *
from ..verificação import *


# mostra as pessoas cadastradas

def pessoas_cadastradas(nome):
    cabecalho('PESSOAS CADASTRADAS')
    arq = open(nome, 'r')
    linhas = arq.readlines()
    if linhas == '':
        print('\033[33mNÃO HÁ NENHUM CADASTRO\033[m')
    for item in linhas:
        if item == '':
            pass
        else:
            subitem = item.strip().split(';')
            print(subitem)
            print('\033[34mNome:\033[m', (36 - len(subitem[0])) * '_', subitem[0])
            print('\033[34mIdade\033[m', (36 - len(subitem[1])) * '_', subitem[1])
            print('=' * 43)

    arq.close()


# cadastra nova pessoa

def cadastro(arq):
    cabecalho('NOVO CADASTRO')

    nome = input('\033[34mNome:\033[m ')
    idade = leiaint('\033[34mIdade:\033[m ')

    try:
        arq = open(arq, 'a')
        arq.write(f'\n{nome.strip()};{str(idade).strip()}')
        print(f'Registro de {nome.strip()} adiconado')
    except:
        print('\033[31mErro desconhecido!')
    finally:
        arq.close()
