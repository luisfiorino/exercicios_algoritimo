# Leitura dos comprimentos dos segmentos de reta
segmento1 = float(input("Digite o comprimento do primeiro segmento de reta: "))
segmento2 = float(input("Digite o comprimento do segundo segmento de reta: "))
segmento3 = float(input("Digite o comprimento do terceiro segmento de reta: "))

# Verificação se é possível formar um triângulo
if (segmento1 < segmento2 + segmento3) and (segmento2 < segmento1 + segmento3) and (segmento3 < segmento1 + segmento2):
    print("É possível formar um triângulo com esses segmentos de reta.")
else:
    print("Não é possível formar um triângulo com esses segmentos de reta.")
