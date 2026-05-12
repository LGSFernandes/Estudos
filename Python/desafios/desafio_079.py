lista = []

while True:
    num = int(input('Digite um número: '))

    if num not in lista:
        lista.append(num)

    resp = str(input('Deseja continuar (S/N)? ')).strip().upper()
    while (resp not in 'SN'):
        resp = str(input('Deseja continuar (S/N)? ')).strip().upper()

    if (resp == 'N'):
        break

lista.sort()

print(f'-=' * 30)

for i, valor in enumerate(lista):
    if i < len(lista) - 1:
        print(f'{valor} → ', end = '')
    else:
        print(f'{valor}')