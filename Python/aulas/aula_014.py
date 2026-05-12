for c in range (1, 5):
    num = int(input('Digite um número (Laço For): '))

print(f'FIM!!! (Laço For)')

n = 1
while (n != 0):
    n = int(input('Digite um número (Laço While): '))

print(f'FIM!!! (Laço While)')

resp = 'S'
number = 0
while (resp == 'S'):
    number = int(input('Digite um número: '))
    resp = str(input('Deseja continuar (S/N)? ')).upper()
print(f'FIM!!!')

numero = 1
par = impar = 0
while (numero != 0):
    numero = int(input('Digite um número: '))
    if (numero != 0):
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Foram digitados {par} números PARES e {impar} números ÍMPARES')