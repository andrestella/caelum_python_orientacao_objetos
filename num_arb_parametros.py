# Não é necessário utilizar exatamente este nome: *args,
# mas é uma convenção na comunidade.

def teste(arg, *args):
    print("primeiro argumento normal: {}".format(arg))
    for arg in args:
        print("outro argumento: {}".format(arg))

teste('python', 'é', 'muito', 'legal')

print('\n')

# Também poderíamos conseguir o mesmo resultado passando um 'list'
# ou 'tuple' de argumentos, acrescido do asterisco:

lista = ["é", "muito", "legal"]
teste('python', *lista)

print('\n')

tupla = ("é", "muito", "legal")
teste('python', *tupla)