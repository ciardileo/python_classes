"""
: = formatador
s - strings
d - int
f - float  
:.(Num)f(Quantidade de casas decimais) -- Float
:(Valor)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

faturamento = 1500
custo = 500
lucro = faturamento - custo
margem = lucro / faturamento

print(f'O lucro foi de {lucro:,}')  # separa a casa do milhar por virgula

print(f'O lucro foi de {lucro:.2f}')  # formatação float, 2 casas decimais

print(f'O lucro foi de {lucro:,.2f}')  # duas formatações juntas

print(f'A margem foi de {margem:.2%}')  # formatação em percentual

# macete para formatação em real
formatado = f'{lucro:_.2f}'
formatado = formatado.replace('.', ',').replace('_', '.')
print(f'O lucro foi de {formatado}')

num1 = 21
print(f'{num1:0>10}') # vai adicionar "0" a esquerda do número até ele ter 10 caracteres

