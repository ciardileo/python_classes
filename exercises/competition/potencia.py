"""
A profa. Vilma preparou uma tarefa de programação sobre a operação de potenciação. Para lembrar, seja um número real n e um número inteiro p igual ou maior do que zero, então a operação de potenciação np tem o valor de n multiplicado por ele mesmo p vezes (se p = 0 o resultado da operação de potenciação é 1). Por exemplo, 23 = 2 x 2 x 2 = 8 e 1020 = 1.

A tarefa preparada pela profa. Vilma foi a seguinte: Escreva um programa para calcular o valor das seguintes expressões contendo operações de potenciação:

24 + 123 + 3003 + 152 + 42
Veja que cada termo das expressões tem a forma np onde n e p são números inteiros e p tem apenas um dígito decimal.

No entanto, quando a profa. Vilma colocou o enunciado da tarefa na Internet, a formatação do enunciado foi corrompida, fazendo com que as expressões aparecessem assim para os alunos:

24 + 123 + 3003 + 152 + 42
Note que por exemplo 24 virou 24, 123 virou 123, 3003 virou 3003 e assim por diante, ou seja, as operações de potenciação desapareceram!

Nesta tarefa, você deve escrever um programa para calcular o valor das expressões da tarefa original da profa. Vilma, sabendo que a formatação do enunciado foi corrompida conforme explicado acima.

Entrada
A primeira linha da entrada contém um número inteiro N, o número de termos da expressão. Cada uma das N linhas seguintes contém um inteiro Ti, indicando um termo da expressão com formatação corrompida.

Saída
Seu programa deve produzir uma linha, contendo um único número inteiro, o valor da soma dos termos da expressão, sabendo que a formatação dos termos foi corrompida como explicado acima.
"""

n = int(input())
termos = list()
soma = int()

for i in range(1, n+1):
	termos.append(input())

for termo in termos:
	soma += int(termo[:-1]) ** int(termo[-1])

print(soma)


