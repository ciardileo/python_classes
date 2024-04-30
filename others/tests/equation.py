import math
import matplotlib.pyplot as plt

start = int(input('X inicial:'))
stop = int(input('X final: '))

ax1 = []
ax2 = []

def eh_primo(n):
    return True
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

soma = 0
for i in range(start, stop):
    
    if eh_primo(i):
       
        x = i
        
        try:
            equation = - (-8*x**3 + x + 13) / (5 + x)
        except ZeroDivisionError:
            print(f'X: {x} -> Erro de divisão por zero')
        finally:
        
            if equation == math.floor(equation):
                ax1.append(x)
                ax2.append(equation)
                print(f'X: {x}, Y: {round(equation)}')
                soma += 1
    # else:
    #     print(f'X: {x}, Y: {equation} é um número decimal')

print(soma)

plt.scatter(ax1, ax2, color='red')
plt.yscale('log')
plt.xscale('log')
plt.title("Soluções inteiras em que X é primo")
plt.xlabel("X (em escala logarítmica)")
plt.ylabel("Y (em escala logarítmica)")
plt.show()