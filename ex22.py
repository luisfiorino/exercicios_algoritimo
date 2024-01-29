#Obtendo o ano atual
ano_atual = int(input('Digite o ano atual: '))

#Obtendo o ano de nascimento do rapaz
ano_nascimento = int(input("Digite o ano de nascimento do rapaz: "))

#Calculando a idade do rapaz
idade = ano_atual - ano_nascimento

#Verificando a situação em relação ao alistamento militar
if idade < 18:
    anos_faltantes = 18 - idade
    print(f"Faltam {anos_faltantes} anos para o alistamento militar.")
elif idade == 18:
    print("Está na idade de se alistar no serviço militar obrigatório!")
else:
    anos_passados = idade - 18
    print(f"Já se passaram {anos_passados} anos do alistamento militar.")
