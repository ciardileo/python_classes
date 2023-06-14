"""
problema2 - estoque
"""


# função que computa a venda
def computa_venda(tipo=1, tamanho=1):
    if estoque[tipo - 1][tamanho - 1] > 0:  # caso o estoque for maior que zero, a venda pode ser efetuada
        estoque[tipo - 1][tamanho - 1] -= 1
        return True
    else:
        return False


# input para saber quantos tipos e tamanhos existem
qtd_tipos = int(input())
qtd_tamanhos = int(input())

# variável que guarda a quantidade de vendas
total_vendas = 0

# lista do estoque
estoque = list()

# adiciona as quantidades de cada peça de roupa a lista do estoque
for tipo in range(1, qtd_tipos + 1):
    estoque.append(list())  # adiciona uma lista dentro da lista para cada tipo de roupa

    for tamanho in range(1, qtd_tamanhos + 1):
        qtd = int(input())
        estoque[tipo - 1].append(qtd)  # adiciona a quantidade de produtos em estoque de certo tipo e tamanho

qtd_pedidos = int(input())  # input da quantidade de pedidos

# identifica o tamanho e tipo do pedido para computar a venda
for pedido in range(0, qtd_pedidos):
    # inputs dos valores
    tipo_pedido = int(input())
    tamanho_pedido = int(input())

    # se a venda puder ser computada (True), adiciona mais um no total de vendas
    if computa_venda(tipo_pedido, tamanho_pedido):
        total_vendas += 1

# saída
print(total_vendas)
