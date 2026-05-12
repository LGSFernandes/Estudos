def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def aumentar (valor = 0, porc = 0, format = False):
    if not porc:
        return valor if format is False else moeda(valor)
    
    else:
        valor = valor + (valor * (porc / 100))

        return valor if format is False else moeda(valor)


def diminuir (valor = 0, porc = 0, format = False):
    if not porc:
        return valor if format is False else moeda(valor)
    
    else:
        valor = valor - (valor * (porc / 100))

        return valor if format is False else moeda(valor)
    

def dobro (valor = 0, format = False):
    valor = valor * 2

    return valor if format is False else moeda(valor)


def metade (valor = 0, format = False):
    valor = valor / 2

    return valor if format is False else moeda(valor)


def linhas():
    print('=' * 34)

def resumo (valor = 0, porcAum = 10, porcRed = 5):
    linhas()
    print(f'RESUMO DO VALOR'.center(34))
    linhas()

    print(f'Preço Analisado: \t{moeda(valor)}')

    linhas()

    print(f'Dobro do Preço: \t{dobro(valor, True)}')
    print(f'Metade do Preço: \t{metade(valor, True)}')
    print(f'{porcAum}% de Aumento: \t{aumentar(valor, porcAum, True)}')
    print(f'{porcRed}% de Redução: \t{diminuir(valor, porcRed, True)}')

    linhas()