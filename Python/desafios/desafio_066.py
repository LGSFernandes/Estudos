cont = 0
soma = 0

while True:
    num = int(input('Digite um número (999 para parar): '))

    if (num == 999):
        break

    soma += num
    cont += 1

print(f'Foram digitados {cont} números. E a soma entre eles é de: {soma}')