"""
básicos de SQL
"""

import sqlite3 as sql

# conexão com o banco
con = sql.connect("database.db")

# cursor pra poder enviar comandos
cursor = con.cursor()

# query
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

# resultado da query
resultado = cursor.fetchall()
print(resultado)

# colunas da tabela - metadados
cursor.execute("SELECT * FROM tb_vendas_dsa")
nomes_colunas = [description[0] for description in cursor.description]
print(nomes_colunas)

# fechamento do cursor e da conexão
cursor.close()
con.close()