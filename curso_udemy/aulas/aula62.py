"""
Dicionários:
{"chave" : "valor"}
"""

idade = {"Léo": 14, "Pedro": 23, "Ricardo": 19}

print(idade.get("Léo"))  # retorna o valor dessa chave
print(idade["Pedro"])

print(idade.values())  # retorna todos os valores

print(idade.items())  # retorna todos os pares

print(idade.keys())  # retorna todas as chaves

idade.pop("Léo")  # apaga o item

idade.popitem()  # apaga o último item

outras_idades = {"Maria": 50, "Marcos": 34}

idade.update(outras_idades)  # concatena os dicionários
