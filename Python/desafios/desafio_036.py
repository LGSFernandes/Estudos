valor = float(input('Qual o preço da casa? R$'))
salario = float(input('Qual o salário? R$'))
anos = int(input('Em quantos anos será pago? '))

meses = anos * 12

mensal = valor / meses

limite = salario * 30 / 100

print(f'Para comprar uma casa de R${valor:.2f} em {anos}, a prestação será de R${mensal:.2f}')

if (mensal > limite):
    print(f'Empréstimo \033[31mnegado\033[m!, pois não pode exceder 30% do salário')
else:
    print(f'Empréstimo \033[33maprovado\033[m!')