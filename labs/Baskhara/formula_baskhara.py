# imports
from math import sqrt

# valores
a = float(input("Qual é o valor do a: "))
b = float(input("Qual é o valor do b: "))
c = float(input("Qual é o valor do c: "))

def baskhara(a, b, c):
    delta = ((b) ** 2) -4 * ((a) * (c))
    x1 = ((-(b) + (sqrt((delta)))) / (2 * (a))) if delta > 0 else None
    x2 = ((-(b) - (sqrt((delta)))) / (2 * (a))) if delta > 0 else None
    return delta, x1, x2

delta, x1, x2 = baskhara(a, b, c)

print(f"O delta é {delta} | Raiz do delta é {delta ** (1/2)}\nO x1 é {x1}\nO x2 é {x2}")
