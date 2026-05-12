lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um número: '))

    lista.append(num)

    resp = str(input(f'Deseja continuar (S/N)? ')).strip().upper()

    if (resp not in 'SN'):
        print('Resposta Inválida. Tente Novamente')
        resp = str(input(f'Deseja continuar (S/N)? ')).strip().upper()

    if (resp == 'N'):
        break

for c in lista:

    if (c % 2 == 0):
        lista_par.append(c)
    elif (c == 1):
        pass
    else:
        lista_impar.append(c)

lista.sort()
lista_par.sort()
lista_impar.sort()

print(f'A lista completa é:')
for pos, c in enumerate(lista):
    if (pos < len(lista) - 1):
        print(f'{c} → ', end = '')
    else:
        print(f'{c}')

print('\n')

print(f'A lista dos pares é:')
for pos, c in enumerate(lista_par):
    if (pos < len(lista_par) - 1):
        print(f'{c} → ', end = '')
    else:
        print(f'{c}')

print('\n')

print(f'A lista dos ímpares é:')
for pos, c in enumerate(lista_impar):
    if (pos < len(lista_impar) - 1):
        print(f'{c} → ', end = '')
    else:
        print(f'{c}')