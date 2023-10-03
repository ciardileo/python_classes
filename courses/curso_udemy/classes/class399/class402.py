"""
MySQL em Python
para utilizar servidores grandes, devemos subir esses servidores em containers
podemos utilizar o Docker para isso, pelo menos no windows é necessária fazer uma configuração
para habilitar a emulação de linux para o servidor (wsl)

depois de configurar o docker, para criar um banco de dados, criamos um arquivo chamado docker-compose.yml
e nele colocamos as configurações do nosso bd

para não deixar as variáveis de enviroment públicas (usuario, senha, host), costumamos usar um arquivo .env,
que salva essas informações e passa para o docker-compose de maneira indireta, permitindo privacidade

comandos do docker:
docker-compose up  => sobe o servidor
docker-compose up -d => sobe o servidor e deixa rodando em background
docker ps => lista os containers ativos
docker ps -a => lista todos os containers
"""

import pymysql
import pymysql.cursors

connection = pymysql.connect(  # cria uma conexão com o servidor MySQL do docker
	host="localhost",
	user="usuario",
	password="senha",
	database="base_de_dados",
	cursorclass=pymysql.cursors.DictCursor  # podemos configurar para o fetch retornar dicionarios
)

cursor = connection.cursor()

# a linguagem do SQL é quase a mesma
# exemplo de crud:

# create:
cursor.execute(
	"CREATE TABLE if not exists customers ( "
	"id INT NOT NULL AUTO_INCREMENT,  "
	"nome VARCHAR(50) NOT NULL, "
	"idade INT, "
	"PRIMARY KEY (id)"
	")"
)

cursor.execute(  # exeutando um insert com placeholder para evitar sql injection
	"INSERT INTO customers "
	"(nome, idade) VALUES (%s, %s)", ("Leonardo", 15)
)

lista_de_argumentos = [["Marcos", 13], ["Enzo", 23], ["Carlão", 39]]
cursor.executemany("INSERT INTO customers (nome, idade) VALUES (%s, %s)", lista_de_argumentos)
# podemos executar muitas queries de uma vez (o número vai depender da quantidade de parâmetros passados para os dois %s


# read
cursor.execute("SELECT * FROM customers WHERE id > 5 OR id = 1")
print(*cursor.fetchall(), sep="\n")

# update
cursor.execute("UPDATE customers SET nome='noname', idade=0 WHERE id > 20")

# delete
# cursor.execute("TRUNCATE TABLE customers")  # limpa a tabela

cursor.execute("DELETE FROM customers WHERE id = 22")  # deleta linha

connection.commit()

cursor.close()
connection.close()
