import moeda

preco = float(input('Digite o valor da Moeda: R$'))

print(f'A Metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'A Dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10% de {moeda.moeda(preco)} é {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 13% de {moeda.moeda(preco)} é {moeda.moeda(moeda.diminuir(preco, 13))}')