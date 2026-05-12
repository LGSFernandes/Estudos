n = int(input('Digite um número: '))

print('\n')
print('=' * 20)
print(f'A tabuada de {n} é:')
print('=' * 20)

for c in range (0, 11):
    print(f'| {c} x {n} = {c * n}     |')
    print('-' * 20)

print('=' * 20)