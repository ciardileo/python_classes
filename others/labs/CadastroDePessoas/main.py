# imports
import sys
import os
from app.design import *
from app.verificação import *
from app.menus import *

arquivo = 'pessoas.txt'

if not os.path.exists(arquivo):
    new = open(arquivo, 'w')
    new.close()
    print('ARQUIVO PESSOAS.TXT FOI CRIADO')


class App:
    def __init__(self):
        # opções
        self.opcs = ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']

        while True:
            cabecalho('MENU PRINCIPAL')

            menu(self.opcs)

            linha()

            self.opcao = leiaopc('\033[34mSua Opção: \033[m', 3)

            if self.opcao == 1:
                pessoas_cadastradas(arquivo)
            elif self.opcao == 2:
                cadastro(arquivo)
            else:
                sys.exit()


if __name__ == '__main__':
    App()
