print("*************************************************")
print("*        Exercícios - Estrutura de Dados        *")
print("*************************************************")

print("***   Exercício 1   ***")

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print(lista)
print("O maior valor da lista é {}.".format(max(lista)))
print("O menor valor da lista é {}.".format(min(lista)))
pares = []
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
print("A lista dos números pares é a seguinte: {}.".format(pares))
n = 0
for valor in lista:
    if valor == lista[0]:
        n += 1
print("O número de ocorrências de {} é {}.".format(lista[0], n))
print("A média dos elementos da lista é {}.".format(sum(lista)/len(lista)))
soma = 0
for valor in lista:
    if valor < 0:
        soma += valor
print("A soma dos valores negativos é {}.".format(soma))



print("\n***   Exercício 2   ***")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")
lista = [nome, sobrenome, idade]
print("{} {}, {} anos.".format(lista[0], lista[1], lista[2]))



print("\n***   Exercício 3   ***")

soma = 0
for valor in range(1, 5):
    nota = int(input("Digite a nota número {}: ".format(valor)))
    print("A nota número {} é {}.".format(valor, nota))
    soma += nota
print("A média das notas é {}.".format(soma/4))



print("\n***   Exercício 4   ***")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")
dados = {"nome":nome, "idade":idade, "cidade":cidade}
print("nome: {}".format(dados["nome"]))
print("idade: {}".format(dados["idade"]))
print("cidade: {}".format(dados["cidade"]))



print("\n***   Exercício 5   ***")

pessoas = []
adicionar = 'sim'
while adicionar == 'sim':
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite sua cidade: ")
    dados = {"nome":nome, "idade":idade, "cidade":cidade}
    pessoas.append(dados)
    adicionar = input("Deseja adicionar mais pessoas? (sim/não): ")
for pessoa in pessoas:
    print("\nnome: {}".format(pessoa["nome"]))
    print("idade: {}".format(pessoa["idade"]))
    print("cidade: {}\n".format(pessoa["cidade"]))