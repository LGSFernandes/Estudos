def descobrir_maior(lst):
    maior_valor = 0
    cont = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    
    for valor in lst:
        print(f'{valor} ', end='')
        if cont == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor
        cont += 1
    
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')

minha_lista = list()

while True:
    num = int(input('Digite um número: '))
    minha_lista.append(num)
    
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break

descobrir_maior(minha_lista)