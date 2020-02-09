print("*************************************")
print("*        Jogo de Adivinhação        *")
print("*************************************")

numero_secreto = 40
total_de_tentativas = 3

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
    elif menor:
        print("Você errou! Seu chute foi menor que o número secreto")

print("Fim do jogo!")