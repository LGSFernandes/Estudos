lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(lanche)
print(f'{lanche[2]}')
print(f'{lanche[:3:]}')
print(f'{lanche[::-1]}')
print(sorted(lanche))

for comida in lanche:
    if (comida == lanche[3]):
        print(f'{comida}', end = '')
    else:
        print(f'{comida} → ', end = '')

print(f'\n')

for pos, comida in enumerate(lanche):
    print(f'Comida: {comida}. Posição: {pos}.')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(f'{c}')
print(f'{d}')

print(f'{len(c)}')
print(f'{c.count(5)}')
print(f'{c.index(8)}')

print(f'{d.index(5, 1)}')


pessoa = ('Luckas', 19, 'M', 70.0)
print(pessoa)
del(pessoa)