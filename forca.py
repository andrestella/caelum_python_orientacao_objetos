print("*******************************")
print("*        Jogo da Forca        *")
print("*******************************")

palavra_secreta = "banana"
letras_acertadas = ["_","_","_","_","_","_"]

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while not acertou and not enforcou:
    chute = input("Qual a letra? ")
    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}."
                    .format(letra, posicao))
                letras_acertadas[posicao] = letra
            posicao += 1     
    else:
        erros += 1
        print("Erro! Total de erros = {}".format(erros))
    acertou = "_" not in letras_acertadas
    enforcou = erros == 7
    print(letras_acertadas)

if acertou:
    print("Você ganhou!")
else:
    print("Você perdeu!")

print("Fim do jogo!")