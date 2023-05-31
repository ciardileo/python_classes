"""
modularização em python
criamos módulos para organizar e estruturar nosso código
pacotes = pastas com módulos
os módulos são reconhecidos a partir dos caminhos do sys.path
todos os pacotes abaixo do caminho atual será reconhecido, mas acima, não
(no módulo importado, podemos fazer o seguinte para definir o que o "*" vai importar:
__all__ = ['variaveis']
)
"""
import sys as s

import class154m  # importa o módulo todo
from class154pck.modulo1 import * # importando um módulo dentro de um pacote

print(*s.path, sep='\n')  # todos os caminhos que o interpretador irá procurar os módulos
s.path.append(r"C:\Users\Léo\ciardi\work\studies\programming\python\classes\courses\curso_udemy\exercises")  # adiciona um caminho

print(class154m.numero)
