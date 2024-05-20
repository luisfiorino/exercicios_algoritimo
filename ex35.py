def calcular_preco_aluguel(tipo_carro, dias_aluguel, km_percorridos):
    # Define os custos de aluguel por dia
    if tipo_carro.lower() == 'popular':
        custo_por_dia = 90
        if km_percorridos <= 100:
            custo_por_km = 0.20
        else:
            custo_por_km = 0.10
    elif tipo_carro.lower() == 'luxo':
        custo_por_dia = 150
        if km_percorridos <= 200:
            custo_por_km = 0.30
        else:
            custo_por_km = 0.25
    else:
        raise ValueError("Tipo de carro inválido. Escolha 'popular' ou 'luxo'.")

    # Calcula o custo total
    custo_total = (custo_por_dia * dias_aluguel) + (custo_por_km * km_percorridos)
    return custo_total

# Entrada de dados
tipo_carro = input("Digite o tipo de carro alugado (popular ou luxo): ").strip()
dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))

# Calcula o preço a ser pago
preco_total = calcular_preco_aluguel(tipo_carro, dias_aluguel, km_percorridos)

# Exibe o resultado
print(f"O preço total a ser pago é: R${preco_total:.2f}")
