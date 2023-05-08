"""
sets em python
sets são conjuntos, não possuem ordem nem index e os elementos não se repetem
são declarados da mesma forma que os dicionários
"""

# criando sets
s1 = set("Leonardo")  # ta iterando a string "leonardo"
s2 = {1, 23, 12, 123, 92}

print(s1)
print(s2)

# funções úteis
s1.add("B")
s2.update("Marcos")
s2.discard("r")

# operações com sets
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}

print(set1 | set2)  # união
print(set1 & set2)  # intersecção
print(set2 - set1)  # diferença (itens apenas presentes no set da esquerda)
print(set1 ^ set2)  # diferença simétrica (itens que não estão nos dois, ou seja, únicos)

