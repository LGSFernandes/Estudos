from random import randint
from time import sleep

numeros = list()

def linhas():
    print('-=' * 20)


def sorteia():
    linhas()
    print('Sorteando 5 valores da lista: ', end='')

    for c in range (0, 5):
        num = randint(1, 10)
        numeros.append(num)

        if c == 4:
            print(f'{num}. ', flush=True)
        else:
            print(f'{num} ', end='', flush=True)

        sleep(0.3)

    print('FIM!!')


def somaPar():

    sorteia()

    soma = 0
    for num in numeros:
        if (num % 2 == 0):
            soma += num

    linhas()
    print(f'Somando os valores pares de {numeros}, temos {soma}.')
    linhas()


somaPar()

