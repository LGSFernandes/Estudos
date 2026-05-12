print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

num = int(input('Quantos termos você quer mostrar? '))

a1 = 0
a2 = 1

print('~' * 30)
print(f'{a1} → {a2}', end='')

cont = 3
while (cont <= num):
    a3 = a1 + a2
    print(f' → {a3}', end='')
    
    a1 = a2
    a2 = a3

    cont += 1

print(' → FIM')
print('~' * 30)