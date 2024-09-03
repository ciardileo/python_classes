def main():
    valor, produtos = map(int, input().split())
    
    def backtrack(R, K, start, current_sum, depth):
        # Se a combinação tem K elementos e soma exatamente R
        if depth == K:
            return 1 if current_sum == R else 0
        
        count = 0
        
        # Limitar o próximo número a ser considerado
        max_value = R - current_sum - (K - depth - 1)
        
        for i in range(start, min(max_value + 1, R + 1)):
            # Se a soma atual mais o próximo número não puder atingir R, paramos
            if current_sum + i > R:
                break
            # Recorremos adicionando o próximo número
            count += backtrack(R, K, i + 1, current_sum + i, depth + 1)
        
        return count

    # Inicializa o processo de backtracking
    result = backtrack(valor, produtos, 1, 0, 0)
    
    print(result)

if __name__ == "__main__":
    main()
