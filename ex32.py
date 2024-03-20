import random # random gera escolhas aleatórias para o computador.

opcoes = ["Pedra", "Papel", "Tesoura"] # Define uma lista contendo as opções do jogo: "Pedra", "Papel" e "Tesoura".

while True:
    escolha_computador = random.choice(opcoes) # Use a função random.choice() para fazer o computador escolher aleatoriamente uma opção da lista.
    escolha_jogador = input("Escolha Pedra, Papel ou Tesoura (ou digite 'sair' para sair): ") # Peça ao jogador para escolher entre as opções e armazene a escolha.

    if escolha_jogador.lower() == "sair":
        print("Obrigado por jogar! Até a próxima!")
        break

    if escolha_jogador not in opcoes:
        print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")
        continue

    print(f"O computador escolheu: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
         (escolha_jogador == "Tesoura" and escolha_computador == "Papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
