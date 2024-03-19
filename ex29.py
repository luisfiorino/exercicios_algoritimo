# Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². O programa também devemostrar a classificação desse terreno, de acordo com a lista abaixo:    
# - Abaixo de 100m² = TERRENO POPULAR
# - Entre 100m² e 500m² = TERRENO MASTER
# - Acima de 500m² = TERRENO VIP

largura = float(input('Digite a largura: '))

comp = float(input('Digite o comprimento: '))

area = largura * comp

if area < 100:
    print('TERRENO POPULAR.')

elif 100 < area < 500:
    print('TERRENO MASTER.')

else:
    print('TERRENO VIP.')