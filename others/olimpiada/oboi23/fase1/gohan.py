
# quantidade de notas
n = int(input())

# notas
h = list()
p = list()

for i in range(1, n + 1):
	val1, val2 = list(map(int, input().split()))

	p.append(val1)
	h.append(val2)

media_h, media_p = sum(h) / len(h), sum(p) / len(p)

if media_h > media_p:
	print(":0 <- Gohan e Feijao")
elif media_h < media_p:
	print(':0 <-X- Gohan e Feijao')
else:
	print("Impasse")


