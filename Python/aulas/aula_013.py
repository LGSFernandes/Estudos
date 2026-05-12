for c in range (0, 6):
    print('Olá')
print('FIM!!')

for c in range (0, 7):
    print(c)
print('FIM!!')

for c in range (6, 0, -1):
    print(c)
print('FIM!!')

for c in range (0, 11, 2):
    print(c)
print('FIM!!')


num = int(input('Digite um número: '))

for c in range (0, num + 1):
    print(c)
print('FIM!!')

ini = int(input('Digite um número: '))
fim = int(input('Digite um número: '))
passo = int(input('Digite um número: '))

for c in range (ini, fim + 1, passo):
    print(c)
print('FIM!!')

soma = 0

for c in range (0, 6):
    soma += num
print(f'O valor total da soma foi de {soma}')