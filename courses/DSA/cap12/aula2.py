"""
Análise de Dados com SQL
"""

import sqlite3 as sql

# conexão e cursor
con = sql.connect("database.db")
cursor = con.cursor()

# agregação - média
cursor.execute("SELECT AVG(Unidades_Vendidas) from tb_vendas_dsa")
print(cursor.fetchall())

# groupby, filter e having - groupby sempre usa uma regra de agregação
# having serve para aplicar um filtro depois do group by, quando os dados já foram selecionados e ordenados
# tradução: selecione Nome_Produto e calcule a média de unidades vendidas dele se o valor dele for maior que 199, agrupando por nome e só mostrando se a média dele for maior que 10
cursor.execute("SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa WHERE Valor_Unitario > 199 GROUP BY Nome_Produto HAVING AVG(Unidades_Vendidas) > 10")
print(*cursor.fetchall(), sep='\n')

# fechar a conexão
cursor.close()
con.close()