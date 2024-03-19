# Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

# Leitura dos comprimentos dos segmentos de reta
segmento1 = float(input("Digite o comprimento do primeiro segmento de reta: "))
segmento2 = float(input("Digite o comprimento do segundo segmento de reta: "))
segmento3 = float(input("Digite o comprimento do terceiro segmento de reta: "))

# Verificação se é possível formar um triângulo e fala o tipo de triângulo formado:
if (segmento1 < segmento2 + segmento3) and (segmento2 < segmento1 + segmento3) and (segmento3 < segmento1 + segmento2):
    print("É possível formar um triângulo com esses segmentos de reta.")
    if segmento1 == segmento2 == segmento3:
        print("O triângulo formado é Equilátero.")
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print("O triângulo formado é Isósceles.")
    else:
        print("O triângulo formado é Escaleno.")
else:
    print("Não é possível formar um triângulo com esses segmentos de reta.")