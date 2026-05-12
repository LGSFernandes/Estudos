fac = 1

num = int(input('Digite um número: '))

if (num > 0):
    for c in range (num, 0, -1):
        fac *= c

print(f'O fatorial de {num} é: {fac}')