def calcular_desconto(valor_compras, sexo):
    if sexo.lower() == "masculino":
        desconto = valor_compras * 0.05
    elif sexo.lower() == "feminino":
        desconto = valor_compras * 0.13
    else:
        desconto = 0
    
    valor_com_desconto = valor_compras - desconto
    return valor_com_desconto

nome = input("Digite o nome do cliente: ")
sexo = input("Digite o sexo do cliente (Masculino/Feminino): ")
valor_compras = float(input("Digite o valor das compras: "))

valor_final = calcular_desconto(valor_compras, sexo)

print(f"Olá, {nome}! O valor final com desconto é: R${valor_final:.2f}")


