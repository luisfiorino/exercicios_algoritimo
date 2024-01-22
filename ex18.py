ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2024 
idade = ano_atual - ano_nascimento

if idade >= 16:
    print(f"Você tem {idade} anos e já pode votar.")
else:
    print(f"Você tem {idade} anos e ainda não pode votar.")