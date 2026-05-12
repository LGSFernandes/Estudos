km = float(input('Quantos km tem a viagem? '))

if(km <= 200):
    preco = 0.50 * km
else:
    preco = 0.45 * km

print(f'O preço da passagem será de R${preco:.2f}')