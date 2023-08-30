"""
SQL em Python
para bases de dados com poucos acessos => sqlite
para bases de dados externas maiores => mysql, oracle, sqlserver...
Servidor => Base de dados => Tabelas
===============================
quando o nome da variável está em caps lock, essa variável é uma constante
"""

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent  # função que retorna o caminho do diretório atual
DB_FILE = ROOT_DIR / 'db.sqlite3'  # essa barra faz com que fique formatado como path

con = sqlite3.connect(DB_FILE)  # abre a conexão
cursor = con.cursor()  # cria um cursor pra executar ações dentro do arquivo

cursor.execute(  # executa comandos SQL
	"CREATE TABLE IF NOT EXISTS customers("  # cria uma tabela caso não existe
	"id INTEGER PRIMARY KEY AUTOINCREMENT,"  # primary key = os elementos serão buscados por essa coluna
	"name TEXT,"
	"weight REAL"
	")"
)

con.commit()  # envia os comandos

# passar os dados juntos da execução do comando é perigoso pois ficamos sujeitos a sqlinjection
# cursor.execute(
# 	"INSERT INTO customers (id, name, weight)"
# 	"VALUES (NULL, 'Leonardo Ciardi', 65.3)"
# )

cursor.execute(  # as bindings (?) serão substituídas em ordem pelos valores na lista
	"INSERT INTO customers (name, weight)"
	"VALUES (?, ?)", ["Leonardo Ciardi", 65.3]
)

# além das bindings, também podemos passar dicionários, para isso basta passar :[nome_da_chave] nos values

con.commit()

cursor.execute("DELETE FROM customers")  # apaga todos os dados da tabela

# devemos sempre fechar o cursor e a conexão
cursor.close()
con.close()
