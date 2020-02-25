# Não é necessário utilizar exatamente este nome: **kwargs,
# mas é uma convenção na comunidade.
# Você deve usar o **kwargs se quiser manipular argumentos nomeados em uma função.

def teste(**kwargs):
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))

teste(nome='caelum')

# Também podemos passar um dicionário acrescido de dois asteriscos (**)
# já que se trata de chave e valor:

dicionario = {'nome': 'andré', 'idade': 40}
teste(**dicionario)

# A diferença é que o *args espera uma tupla de argumentos posicionais
# enquanto o **kwargs um dicionário com argumentos nomeados.