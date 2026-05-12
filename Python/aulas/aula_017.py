num = [2, 5, 9, 1]

for c in num:
    if(c == num[3]):
        print(f'{c}')
    else:
        print(f'{c}, ', end = '')

num[2] = 3

for c in num:
    if(c == num[3]):
        print(f'{c}')
    else:
        print(f'{c}, ', end = '')

num.append(7)

for c in num:
    if(c == num[4]):
        print(f'{c}')
    else:
        print(f'{c}, ', end = '')

num.sort()

for c in num:
    if(c == num[4]):
        print(f'{c}')
    else:
        print(f'{c}, ', end = '')

num.sort(reverse = True)

for c in num:
    if(c == num[4]):
        print(f'{c}')
    else:
        print(f'{c}, ', end = '')

num.insert(2, 3)

for c in num:
    if(c == num[5]):
        print(f'{c}')
    else:
        print(f'{c}, ', end = '')

if 5 in num:
    num.remove(5)

    for c in num:
        if(c == num[4]):
            print(f'{c}')
        else:
            print(f'{c}, ', end = '')

else:
    print('Não tem o número 5 na lista')


valores = []

for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

    if (v == 67):
        print('SIX SEVEN 🖐 6️⃣  7️⃣ 🖐')

print('Fim da lista')


a = [2, 3, 4, 7]

b = a 
    # Cria uma ligação entre a lista A e a lista B (Mudar uma irá mudar a outra)

b = a[:] 
    # Cria uma cópia da lista A para a lista B (Pode alterar uma sem mudar a outra)

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')