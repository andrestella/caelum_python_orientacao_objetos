print("********************************************************")
print("*        Exercícios - Funções (*args e **kwargs)       *")
print("********************************************************")

print("***   Exercício 1   ***")

def teste_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

teste_args_kwargs(10, 20, 30)



print("***   Exercício 2   ***")

args = ('um', 2, 3)
teste_args_kwargs(*args)



print("***   Exercício 3   ***")

kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}
teste_args_kwargs(**kwargs)



print("***   Exercício 4   ***")

# Os código abaixo geram um 'TypeError'.

# args = ('andré', 'alexandre', 'stella', 40)
# teste_args_kwargs(*args)

# kwargs = {'arg3': 100, 'arg2': 200, 'arg1': 100, 'arg0': 'zero'}
# teste_args_kwargs(**kwargs)



print("***   Exercício 5   ***")

def teste_args_kwargs(*args):
    n = 1
    while n <= len(args):
        print("arg{}: {}".format(n, args[n-1]))
        n += 1

args = ('andré', 'alexandre', 'stella', 40)
teste_args_kwargs(*args)


def teste_args_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

kwargs = {'arg3': 100, 'arg2': 200, 'arg1': 100, 'arg0': 'zero'}
teste_args_kwargs(**kwargs)