print("*************************************")
print("*        Jogo de Adivinhação        *")
print("*************************************")

numero_secreto = 40
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
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
    elif menor:
        print("Você errou! Seu chute foi menor que o número secreto")

    rodada = rodada + 1

print("Fim do jogo!")