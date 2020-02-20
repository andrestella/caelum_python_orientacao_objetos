print("**************************************")
print("*        Exercícios - Funções        *")
print("**************************************")

print("***   Exercício 1   ***")

def velocidade_media(distancia, tempo):
    pass



print("***   Exercício 2   ***")

def velocidade_media(distancia, tempo):
    velocidade = distancia / tempo



print("***   Exercício 3   ***")

def velocidade_media(distancia, tempo):
    velocidade = distancia / tempo
    print(velocidade)



print("***   Exercício 4   ***")

velocidade_media(100, 20)
velocidade_media(150, 22)
velocidade_media(200, 30)
velocidade_media(50, 3)



print("***   Exercício 5   ***")

def velocidade_media(distancia, tempo):
    velocidade = distancia / tempo
    return velocidade



print("***   Exercício 6   ***")

def soma(num_1, num_2):
    soma = num_1 + num_2
    return soma



print("***   Exercício 7   ***")

def subtracao(num_1, num_2):
    subtracao = num_1 - num_2
    return subtracao



print("***   Exercício 8   ***")

def calculadora(num_1, num_2):
    soma = num_1 + num_2
    subtracao = num_1 - num_2
    return soma, subtracao



print("***   Exercício 9   ***")

def calculadora(num_1, num_2):
    soma = num_1 + num_2
    subtracao = num_1 - num_2
    multiplicacao = num_1 * num_2
    divisao = num_1 / num_2
    # return soma, subtracao, multiplicacao, divisao
    return {'soma': soma,
            'subtracao': subtracao,
            'multiplicacao': multiplicacao,
            'divisao': divisao}



print("***   Exercício 10   ***")

calculos = calculadora(20, 5)
# for calculo in calculos:
#     print(calculo)
for key in calculos:
    print("{}: {}".format(key, calculos[key]))



print("***   Exercício 11   ***")

def divisao(num_1, num_2):
    if num_2 == 0:
        return None
    else:
        divisao = num_1 / num_2
        return divisao

def velocidade_media(distancia, tempo):
    velocidade = divisao(distancia, tempo)
    if velocidade is not None:
        print("velocidade média: {} m/s".format(velocidade))

velocidade_media(100, 20)
velocidade_media(-20, 10)
velocidade_media(150, 0)