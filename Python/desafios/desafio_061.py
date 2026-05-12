a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA?'))

a10 = a1 + (10 - 1) * r

while (a1 != a10):
    print(f'{a1} → ', end = '')
    a1 = a1 + r
