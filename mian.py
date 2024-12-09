def contar_pares_e_impares(lista):
    # Filtrando números pares e ímpares usando filter
    pares = list(filter(lambda x: x % 2 == 0, lista))
    impares = list(filter(lambda x: x % 2 != 0, lista))
    
    # Retornando as contagens de pares e ímpares
    return len(pares), len(impares)

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = contar_pares_e_impares(numeros)

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
