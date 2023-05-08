numero_produtos = int(input("Quantos produtos você quer adicionar?: "))

carrinho = []

for i in range(0, numero_produtos):
	nome, preco = input(f"{i+1} | Nome do produto: "), float(input(f"{i + 1} | Preço do produto (R$): "))
	carrinho.append((nome, preco))

soma = sum([float(x[1]) for x in carrinho])
print(f'A soma dos preços de todos os produtos é R${soma}')
