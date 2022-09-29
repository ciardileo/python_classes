counter1, counter2 = 0, 10

print(f'[C1] {counter1} [C2] {counter2}')

while counter1 < 10 and counter2 > 0:
	counter2 -= 1
	counter1 += 1
	print(f'[C1] {counter1} [C2] {counter2}')

##########################################################

for c, d in enumerate(range(10, -1, -1)):
	print(c, d)

'''
O c é o contador crescente, que receberá o valor de índice do enumerate, que vai em ordem crescente
Já o d, é o decrescente que receberá o valor do range, que vai do 10 ao -1 (lembrando que o índice sempre é um a menos do que o indicado)
'''