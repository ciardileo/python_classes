"""
modularização em python
criamos módulos para organizar e estruturar nosso código
pacotes = pastas com módulos
os módulos são reconhecidos a partir dos caminhos do sys.path
todos os pacotes abaixo do caminho atual será reconhecido, mas acima, não
as importações são sempre relativas ao __main__
o arquivo __init__ será executado toda vez que o módulo for executado
(no módulo importado, podemos fazer o seguinte para definir o que o "*" vai importar:
__all__ = ['variaveis']
)
"""
import sys as s

import class154m  # importa o módulo todo

print(*s.path, sep='\n')  # todos os caminhos que o interpretador irá procurar os módulos
s.path.append(r"/courses/curso_udemy/exercises")  # adiciona um caminho

print(class154m.numero)
