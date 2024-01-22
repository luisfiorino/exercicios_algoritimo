velocidade = int(input('Qual a velocidade? '))
velocidade_maxima = 80

if velocidade > velocidade_maxima:
    multa = (velocidade - velocidade_maxima) * 5
    
    print(f"Você foi multado! Velocidade: {velocidade} Km/h. Multa: R${multa:.2f}")
else:
    print("Velocidade dentro do limite permitido. Dirija com segurança!")