original = float(input('Digite o preço do produto: '))
desconto = (5 * original) / 100
promocional = original - desconto

print(f'O preço do produto e de R${original:.2f}, com o desconto de 5% ele sai a R${promocional:.2f}.')