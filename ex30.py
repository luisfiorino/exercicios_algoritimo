# Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%

# Entradas do usuário
nome = input("Digite o nome do funcionário: ")
salario_atual = float(input("Digite o salário atual do funcionário: "))
anos_trabalhados = int(input("Digite quantos anos o funcionário trabalha na empresa: "))

# Determinar o percentual de aumento
if anos_trabalhados <= 3:
    aumento = 3
elif 3 <= anos_trabalhados <= 10:
    aumento = 12.5
else:
    aumento = 20

# Calcular o novo salário
novo_salario = salario_atual * (1 + aumento / 100)

# Exibir resultados
print(f"Nome do funcionário: {nome}")
print(f"Salário antigo: R${salario_atual:.2f}")
print(f"Percentual de aumento: {aumento}%")
print(f"Novo salário: R${novo_salario:.2f}")
