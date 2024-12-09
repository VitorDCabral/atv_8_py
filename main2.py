vendas_trimestrais = [
    [1500, 2000, 1800],  # Trimestre 1: Janeiro, Fevereiro, Março
    [2200, 2500, 2400],  # Trimestre 2: Abril, Maio, Junho
    [2100, 2200, 2300],  # Trimestre 3: Julho, Agosto, Setembro
    [2700, 2800, 2900]   # Trimestre 4: Outubro, Novembro, Dezembro
]

def analise_vendas(vendas_trimestrais):
    # Calculando a média de vendas por trimestre
    medias_trimestrais = [sum(trimestre) / len(trimestre) for trimestre in vendas_trimestrais]

    # Encontrando o trimestre com a maior soma de vendas
    soma_vendas_por_trimestre = [sum(trimestre) for trimestre in vendas_trimestrais]
    trimestre_maior_venda = soma_vendas_por_trimestre.index(max(soma_vendas_por_trimestre)) + 1

    # Encontrando o trimestre com a menor soma de vendas
    trimestre_menor_venda = soma_vendas_por_trimestre.index(min(soma_vendas_por_trimestre)) + 1

    # Calculando o total de vendas no ano inteiro
    total_vendas_ano = sum(soma_vendas_por_trimestre)

    return medias_trimestrais, trimestre_maior_venda, trimestre_menor_venda, total_vendas_ano

# Dados fictícios de vendas trimestrais
vendas_trimestrais = [
    [1500, 2000, 1800],  # Trimestre 1
    [2200, 2500, 2400],  # Trimestre 2
    [2100, 2200, 2300],  # Trimestre 3
    [2700, 2800, 2900]   # Trimestre 4
]

# Analisando as vendas
medias, trimestre_maior, trimestre_menor, total_ano = analise_vendas(vendas_trimestrais)

# Exibindo os resultados
print("Média de vendas por trimestre:", medias)
print(f"Trimestre com a maior soma de vendas: Trimestre {trimestre_maior}")
print(f"Trimestre com a menor soma de vendas: Trimestre {trimestre_menor}")
print(f"Total de vendas no ano inteiro: R${total_ano}")
