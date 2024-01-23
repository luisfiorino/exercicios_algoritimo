nome = input('Qual e seu nome? ')

nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f'{nome} você foi aprovado, suas notas foram {nota1:.2f} pontos e {nota2:.2f} pontos dando uma media de {media:.2f} pontos')
else:
    print(f'{nome} você foi reprovado, sua media foi de {media:.2f} pontos.')