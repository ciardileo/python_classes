a = 2 
b = 1 

for n in range(2, 100):
    ax = a + 2*b
    bx = b - 4*a
    print(f'A: {ax}; B: {bx}')
    a, b = ax, bx