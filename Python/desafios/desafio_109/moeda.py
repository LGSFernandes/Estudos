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