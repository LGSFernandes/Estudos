lista = []

for c in range (0, 5):
    num = int(input('Digite um número: '))

    if (type(num) != int):
        print('Formato inválido. Tente novamente!')
        num = int(input('Digite um número: '))

    if (c == 0 or num > lista[-1]):
        lista.append(num)
    else:
        pos = 0

        while (pos < len(lista)):

            if (num <= lista[pos]):
                lista.insert(pos, num)
                break

            pos += 1

print('-=' * 30)

for i, valor in enumerate(lista):
    if (i < len(lista) - 1):
        print(f'{valor} → ', end = '')
    else:
        print(valor)