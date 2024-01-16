cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))

total_cigarros = cigarros * 365 * anos
tempo_perdido_minutos = total_cigarros * 10

tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)

print(f"Um fumante perderá aproximadamente {tempo_perdido_dias:.0f} dias de vida.")