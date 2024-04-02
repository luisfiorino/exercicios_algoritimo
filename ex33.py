
# Solicitação dos dados de entrada ao usuário
valor_casa = float(input("Qual o valor do imovel? "))
salario_comprador = float(input("Qual e a sua renda? "))
anos_pagamento = int(input("Em quantos anos será o pagamento: "))

# Calcula o valor da prestação mensal
prestacao_mensal = valor_casa / (anos_pagamento * 12)

# Verifica se a prestação mensal excede 30% do salário
limite_prestacao = salario_comprador * 0.3

if prestacao_mensal <= limite_prestacao:
    print("Empréstimo aprovado!")
    print(f"O valor da prestação mensal será de R${prestacao_mensal:.3f}.")
else:
    print("Empréstimo negado. O valor da prestação excede 30% do salário.")