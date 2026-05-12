from random import randint

lista = ()

for c in range (1, 6):
    num = (randint(0, 10),)
    lista += num

    if (c == 1):
        maior = num[0]
        menor = num[0]
    else:
        if (num[0] > maior):
            maior = num[0]
        if (num[0] < menor):
            menor = num[0]

    
print(f'A lista dos números é: {lista}')
print(f'Maior valor: {maior}. Menor valor: {menor}')