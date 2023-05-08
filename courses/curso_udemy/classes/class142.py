"""
função isinstance()
retorna se tal valor é de tal tipo
"""

lista = [
	1, 'leo', True, False, 23, 44, (2, 3), {1, 32}, {"carro": "toyota"}, 'Marcos'
]

for item in lista:
	print(f'{item} é string? {isinstance(item, str)}')  # retorna True caso o valor for uma string
