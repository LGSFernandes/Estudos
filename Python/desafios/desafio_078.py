lista = []
maior = menor = 0

for cont in range (0, 5):
    lista.append(int(input('Digite um valor: ')))

    if (type(cont) != int):
        print('Digite um número! Tente novamente')
        lista.append(int(input('Digite um valor: ')))

    if (cont == 0):
        maior = lista[0]
        menor = lista[0]

    if (lista[cont] > maior):
        maior = lista[cont]
    if (lista[cont] < menor):
        menor = lista[cont]


print(f'Maior valor: {maior} e sua posição na lista foi {lista.index(maior) + 1}')
print(f'Menor valor: {menor} e sua posição na lista foi {lista.index(menor) + 1}')