num = 0
cont = 0
soma = 0

while (num != 999):
    num = int(input('Digite um número: '))

    if (num != 999):
        cont += 1
        soma += num

print(f'Foram digitados {cont} números e a soma entre eles foi: {soma}')