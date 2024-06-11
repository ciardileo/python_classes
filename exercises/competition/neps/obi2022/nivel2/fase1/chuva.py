"""
achar o número de intervalos em uma sequencia de numeros que tem a soma igual a S
"""

def main():
    N = int(input())
    S = int(input())
    
    measurements = [int(x) for x in input().split()]
    
    cumulative_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + measurements[i - 1]
    
    count = 0
    for i in range(0, N + 1):
        for j in range(i + 1, N + 1):
            if cumulative_sum[j] - cumulative_sum[i] == S:
                count += 1
        
    print(count)
        
    
if __name__ == "__main__":
    main()