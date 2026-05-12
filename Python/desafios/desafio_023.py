num = int((input('Escolha um número de 0 a 9999: ')))


mil = num // 1000 % 10
cen = num // 100 % 10
dez = num // 10 % 10
uni = num // 1 % 10

print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')