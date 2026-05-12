import moeda

preco = float(input('Digite o valor da Moeda: R$'))

print(f'A Metade de {preco} é {moeda.metade(preco)}')
print(f'A Dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10% de {preco} é {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 13% de {preco} é {moeda.diminuir(preco, 13)}')