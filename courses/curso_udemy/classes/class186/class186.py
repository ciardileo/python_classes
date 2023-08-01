"""
criação e manipulação de arquivos em Python
MODOS DE ABERTURA:
r - read
w - write (se não houver um arquivo, ele será criado) (apaga todo o arquivo antes de escrever)
a - append (escreve no arquivo a partir da última linha)
x - create
b - binary
caso usarmos um + depois, o arquivo poderá ser lido e escrito também
CAMINHOS
no windows, as barras de um caminho são ao contrário, o que gera certos problemas para o Python, para contornar isso, podemos colocar barras duplas ou colocar um 'r' antes das aspas da string
CURSOR
durante a abertura de arquivos, o Python possui uma espécie de cursor nas linhas dos arquivos, por isso, dependendo de onde o cursor está, pode ser que a função read() só retorne parte do arquivo ou nada
"""

file_path = r"C:\Users\leoci\ciardi\work\studies\programming\python\classes\courses\curso_udemy\classes\class186\class186.txt"

# file = open(file_path, 'r')
#
# file.close()  # todo arquivo deve ser fechado para evitar problemas


# podemos usar um bloco with, chamado de context manager, que abre e fecha o arquivo automaticamente
with open(file_path, "w") as arquivo:
	arquivo.write("first line\n")  # escreve no arquivo (na sequência de onde está o cursor)
	arquivo.write("second line\n")

	arquivo.seek(0, 0)  # move o cursor do arquivo para a linha 0 coluna 0

	arquivo.writelines(("linha1\n",
	                    "linha2\n"))  # é um write que recebe um iterável como parâmetro (as linhas têm que ser quebradas manualmente)

with open(file_path, "r",
          encoding="utf8") as arquivo:  # também podemos mudar a codificação padrão do arquivo para que ele aceite mais caracteres
	print(arquivo.read())  # lê o arquivo todo

	arquivo.seek(0, 0)
	arquivo.readline()  # funciona como um next, lê a próxima linha em relação ao cursor

	for linha in arquivo.readlines():  # função que retorna uma lista de todas as linhas do arquivo
		print(linha)

# =============================================

# funções úteis com arquivos do módulo OS
import os

os.rename(file_path, "testando.txt")  # renomeia o arquivo, também pode ser usado para mover

# os.remove(file_path)  # exclui o arquivo
# os.unlink(file_path)  faz a mesma função do remove
