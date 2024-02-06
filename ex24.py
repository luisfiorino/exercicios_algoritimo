def calcular_preco_passagem(distancia_km):
    if distancia_km <= 200:
        preco_passagem = distancia_km * 0.50
    else:
        preco_passagem = distancia_km * 0.45
    return preco_passagem

distancia_desejada = float(input("Digite a distância que deseja percorrer em Km: "))
preco_final = calcular_preco_passagem(distancia_desejada)

print(f"O preço da passagem para {distancia_desejada} Km é de R${preco_final:.2f}")
