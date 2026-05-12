matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

soma_pares = soma_coluna = maior_segunda = 0

for linha in range(0, 3):
    for coluna in range (0, 3):

        if (matriz[linha][coluna] % 2 == 0):
            soma_pares += matriz[linha][coluna]

for linha in range (0, 3):
    soma_coluna += matriz[linha][2]

for coluna in range (0, 3):
    if (coluna == 0):
        maior_segunda += matriz[1][coluna]
    elif (matriz[1][coluna] > maior_segunda):
        maior_segunda = matriz[1][coluna]

print(f'Soma de todos valores pares: {soma_pares}')
print(f'Soma dos termos da terceira coluna: {soma_coluna}')
print(f'Maior valor da segunda linha: {maior_segunda}')
