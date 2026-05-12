cont = total = preco_barato = caro = 0

while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? R$'))

    cont += 1

    total += preco

    if (preco > 1000):
        caro += 1
    
    if (cont == 1):
        barato = nome
        preco_barato = preco
    else:
        if (preco < preco_barato):
            barato = nome

    resp = str(input('Deseja continuar (S/N) ? ')).upper()

    if (resp not in ['S', 'N']):
        print(f'Resposta inválida. Tente novamente: ')
        resp = str(input('Deseja continuar (S/N) ? ')).upper()
    else:
        if (resp == 'N'):
            break

print(f'O total gasto será de R${total:.2f}')

if (caro == 1):
    print(f'{caro} produto custa mais de R$1000.00')
else:
    print(f'{caro} produtos custam mais de R$1000.00')

print(f'O nome do produto mais barato é: {barato}')