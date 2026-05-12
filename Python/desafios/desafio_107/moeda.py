def aumentar (valor, porc = 0):
    if not porc:
        return valor
    
    else:
        valor = valor + (valor * (porc / 100))

        return valor
    
def diminuir (valor, porc = 0):
    if not porc:
        return valor
    
    else:
        valor = valor - (valor * (porc / 100))

        return valor
    
def dobro (valor):
    return valor * 2

def metade (valor):
    return valor / 2