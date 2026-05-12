num = 0
soma = 0

while True:
    num = int(input('Digite um número: '))

    if (num == 999):
        break

    soma += num

print(f'A soma dos valores foi de: {soma}')