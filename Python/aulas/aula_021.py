help(input)

print(input.__doc__)

def contador (i, f, p):

    """
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """

    c = i

    while c <= f:
        print(f'{c} ', end='')
        c += p
    
    print('FIM!')

contador(2, 10, 2)
help(contador)

def somar(a = 0, b = 0, c = 0):
    """
        -> Faz a soma de três valores e mostra o resultado na tela.
        :param a: o primeiro valor
        :param b: o segundo valor
        :param c: o terceiro valor
        :return: sem retorno
    """

    s = a + b + c
    print(f'A soma vale {s}.')

somar(3, 2)


def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


# Programa principal
n = 2
print(f'No programa principal, n vale {n}.')

teste()

x = 5

print(f'No programa principal, x vale {x}.')



def calc(a = 0, b = 0, c = 0):
    s = a + b + c

    return s

r1 = calc(3, 2, 5)
r2 = calc(2, 6)
r3 = calc(4)

print(f'Os resultados foram {r1}, {r2} e {r3}.')

def fatorial(num = 1):
    f = 1

    for c in range (num, 0, -1):
        f *= c

    return f

n = int(input('Digite um número para calcular seu fatorial: '))

print(f'O fatorial de {n} é igual a {fatorial(n)}.')

def parOuImpar(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False
    
numero = int(input('Digite um número para saber se ele é par ou ímpar: '))

if parOuImpar(numero):
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')