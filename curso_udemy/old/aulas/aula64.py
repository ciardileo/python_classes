"""
os sets são declarados da mesma forma que os dicionários (chaves)
sets não aceitam elementos duplicados - normalmente são usados para isso
tem funções específicas relacionadas ao diagrama de venn
os elementos do set embaralham a ordem
"""

set1 = set()
set2 = {1, 2, 3, 4, 5}  # ambos são jeitos de criar sets

# ========================================================

lista1 = [1, 2, 33, 2, 1, 33, 1, 2, "léo", "léo"]
print(lista1)
set_lista = set(lista1)
print(set_lista)
lista1 = list(set_lista)
print(lista1)

# =========================================================

set_lista.add("Na")  # adiciona um elemento ao set
set_lista.update("Na")  # similar ao add(), porém itera o elemento antes de adicionar (nao adciona em ordem)
set_lista.discard("Na")  # remove o elemento (não é por index)
set_lista.clear()  # limpa o set

# =========================================================

l1 = {1, 2, 3, 4, 5, 6}
l2 = {1, 2, 3, 4}

l3 = l1 | l2  # une os dois conjuntos
l3 = l1.union(l2)
print(l3)

l3 = l1 - l2  # mostra elementos que só o set da esquerda possui
l3 = l1.difference(l2)
print(l3)

l3 = l1 & l2  # mostra elementos que estão nos dois sets
l3 = l1.intersection(l2)
print(l3)

# =========================================================

set1 = {2, 1, 3}
print(set1)
set1.add(1)
print(set1)

# =========================================================


