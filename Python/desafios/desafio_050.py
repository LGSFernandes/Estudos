soma = 0

for c in range (0, 7):
    n = int(input('Digite um número: '))

    if (n % 2 == 0):
        soma += n
    
print(f'A soma total foi de {soma}')