resp = 'S'
cont = 0
soma = 0
maior = menor = 0

while (resp == 'S'):
    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar (S/N)? ')).upper()
    
    cont += 1
    soma += num
    
    if (cont == 1):
        maior = num
        menor = num
    
    if (num > maior):
        maior = num
    if (num < menor):
        menor = num

media = soma / cont

print(f'A média entre {cont} foi de: {media}')
print(f'O maior valor foi de: {maior}')
print(f'E o menor valor foi de {menor}')

