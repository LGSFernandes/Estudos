a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))

print(f'Os 10 primeiros termos dessa PA são: ')

for c in range (a1, a1 + (10 - 1) * r, r):
    print(c)