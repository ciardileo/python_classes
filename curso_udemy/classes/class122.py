"""
Shallow Copy = Cópia rasa de um dicionário, seus objetos aninhados não são copiados propriamente, apenas são referenciados aos dois dicionários
Deep Copy = O dicionário e todos os seus valores são inteiramente copiados, utiliza mais memória
"""

import copy

dict1 = {
	"v1": 1000,
	"v2": 2300,
	"v4": 1000,
	"lista de valores": [1, 200, 34]
}

# shallow copy com a função dict.copy()
dict2 = dict1.copy()
dict1['lista de valores'][1] = 23
print(dict2['lista de valores'][1])

# deep copy com o módulo importado
dict2 = copy.deepcopy(dict1)
dict1['lista de valores'][0] = 2
print(dict2['lista de valores'][0])


