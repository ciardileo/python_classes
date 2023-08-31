"""
CRUD no SQL:
Create - INSERT
Read - SELECT
Update - UPDATE
Delete - DELETE
"""

import sqlite3
from class387 import DB_FILE

con = sqlite3.connect(DB_FILE)  # abre a conexão
cursor = con.cursor()  # cria um cursor pra executar ações dentro do arquivo

cursor.execute(  # dá update em um dado da tabela que tem id = 1
	"UPDATE customers "
	"SET name='Léo Ciardi', weight=66 "
	"WHERE id=1"
)

con.commit()

cursor.execute("SELECT * FROM customers")  # busca tudo da tabela

print(cursor.fetchone())  # também podemos retornar só um valor

for row in cursor.fetchall():  # retorna os valores em um iterável
	print(row)


# devemos sempre fechar o cursor e a conexão
cursor.close()
con.close()
