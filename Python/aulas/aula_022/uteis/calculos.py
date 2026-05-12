def fatorial (n):
    f = 1

    if n == 1:
        return f
    else: 
        for c in range (n, 0, -1):
            f *= c

    return f


def dobro (n):
    return n * 2

def triplo (n):
    return n * 3