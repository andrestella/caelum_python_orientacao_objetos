print("*************************************")
print("*        Jogo de Adivinhação        *")
print("*************************************")

def jogar():
    nivel = int(input("Escolha o nível -  1, 2 ou 3: "))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    print("Você escolheu o nível {}. Você tem {} tentativas!"
        .format(nivel, total_de_tentativas))

    pontos = 100
    print("Você possui {} pontos".format(pontos))

    numero_secreto = 40

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número: "))
        print("Você digitou {}".format(chute))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou")
            break
        elif maior:
            print("Você errou! Seu chute foi maior que o número secreto")
            pontos = pontos - abs(chute - numero_secreto)
            print("Você está agora com {} pontos".format(pontos))
        elif menor:
            print("Você errou! Seu chute foi menor que o número secreto")
            pontos = pontos - abs(chute - numero_secreto)
            print("Você está agora com {} pontos".format(pontos))

    print("Você ficou com {} pontos".format(pontos))
    print("Fim do jogo!")

jogar()