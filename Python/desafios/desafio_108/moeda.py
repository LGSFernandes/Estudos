def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def aumentar (valor = 0, porc = 0):
    if not porc:
        return valor
    
    else:
        valor = valor + (valor * (porc / 100))

        return valor


def diminuir (valor = 0, porc = 0):
    if not porc:
        return valor
    
    else:
        valor = valor - (valor * (porc / 100))

        return valor
    

def dobro (valor = 0):
    return valor * 2


def metade (valor = 0):
    return valor / 2