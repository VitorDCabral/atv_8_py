vendas = {
    "Produto A": 150,
    "Produto B": 200,
    "Produto C": 200,
    "Produto D": 180
}

def produto_mais_vendido(vendas):
    # Encontrando o valor máximo de vendas
    max_vendas = max(vendas.values())
    
    # Encontrando os produtos que têm esse valor de vendas
    produtos_mais_vendidos = [produto for produto, vendas_totais in vendas.items() if vendas_totais == max_vendas]
    
    return produtos_mais_vendidos

# Exemplo de uso
vendas = {
    "Produto A": 150,
    "Produto B": 200,
    "Produto C": 200,
    "Produto D": 180
}

resultados = produto_mais_vendido(vendas)
print("Produto(s) mais vendido(s):", resultados)


