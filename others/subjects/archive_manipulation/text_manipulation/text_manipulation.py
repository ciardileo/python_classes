# r - read
# w - write
# r+ - read and write
# a - append

archive = open('teste.txt', 'r+')  # se não existir, ele criará o arquivo

archive.write('Testando os arquivos')
archive.writelines(['Escrevendo', 'Em', 'Linhas', 'Diferentes'])

for line in archive:
	print(line)

archive.close()