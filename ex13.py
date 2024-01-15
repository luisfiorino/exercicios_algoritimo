salario = float(input('Digite seu salario: '))
aumento = (15 * salario) / 100
salario_atual = salario + aumento

print(f'Seu salario e de R${salario:.2f}, com o aumento de 15% passara a ser de R${salario_atual:.2f}.')