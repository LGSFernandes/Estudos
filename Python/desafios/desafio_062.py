a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))

a10 = (a1 + (10 - 1) * r) + r

while (a1 != a10):
    print(f'{a1} → ', end = '')
    a1 = a1 + r

resp = int(input('\nDeseja mostrar mais alguns termos (Diga quantos termos deseja, ou 0 para encerrar)? '))
an = (a10 + (resp - 1) * r) + r

if (resp != 0):
    while (a10 != an):
        print(f'{a10} → ', end = '')
        a10 = a10 + r

print(f'Programa encerrado!')