import moeda

preco = float(input('Digite o valor da Moeda: R$'))

print(f'A Metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'A Dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10% de {moeda.moeda(preco)} é {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 13% de {moeda.moeda(preco)} é {moeda.diminuir(preco, 13, True)}')