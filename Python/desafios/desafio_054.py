from datetime import date

menor = 0
maior = 0

for c in range (1, 8):
    nasc = int(input('Em que ano você nasceu? '))

    idade = date.today().year - nasc

    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'{menor} pessoas são menores de idade')
print(f'{maior} pessoas são maiores de idade')