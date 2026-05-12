preco = float(input('Qual o preço do item? R$'))

desconto = preco * 5 / 100

print(f'O novo preço será de R${(preco - desconto):.2f}')