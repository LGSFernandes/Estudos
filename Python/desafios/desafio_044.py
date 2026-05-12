preco = float(input('Qual preço do produto? R$'))
cond = str(input('Qual tipo de compra? ')).upper()

if (cond == 'A VISTA DINHEIRO' or cond == 'A VISTA CHEQUE'):
    preco = preco - (preco * 10 / 100)
    print(f'O preço, {cond.lower()}, será de R${preco:.2f}')
elif (cond == 'A VISTA CARTÃO'):
    preco = preco - (preco * 5 / 100)
    print(f'O preço, {cond.lower()}, será de R${preco:.2f}')
elif (cond == '2X CARTÃO'):
    print(f'O preço, em {cond.lower()}, será de R${preco:.2f}')
else:
    preco = preco + (preco * 20 / 100)
    print(f'O preço, em {cond.lower()}, será de R${preco:.2f}')
