lista = (int(input('Digite um número: ')),
        int(input('Digite outro: ')),
        int(input('Digite mais um: ')),
        int((input('Digite o último: '))))

if (9 in lista):

    if (lista.count(9) == 1):
        print(f'O número 9 foi digitado {lista.count(9)} vez')
    else:
        print(f'O número 9 foi digitado {lista.count(9)} vezez')

else:
    print(f'Não foi digitado número 9 na lista')

if (3 in lista):
    print(f'O número 3 foi digitado pela primeira vez na lista no índice: {lista.index(3) + 1}')
else:
    print(f'Não foi digitado o número 3 na lista')

print(f'Os números pares digitados foram: ', end = '')
for c in lista:
    if (c % 2 == 0):
        print(f'{c} ', end = '')