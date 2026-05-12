colc = ('Bragantino', 'Palmeiras', 'Chapecoense', 'Mirassol', 'Fluminense', 'Bahia', 
        'São Paulo', 'Botafogo', 'Grêmio', 'Atlético-PR', 'Coritiba', 'EC Vitória', 
        'Flamengo', 'Atlético-MG', 'Vasco da Gama', 'Internacional', 'Santos', 
        'Remo', 'Corinthians', 'Cruzeiro')

print('Os cinco primeiros colocados foram: ')

for pos in colc[:5]:
    if (pos == colc[4]):
        print(f'{pos}', end = '')
    else:
        print(f'{pos} → ', end = '')

print('\n')

print('Os quatro últimos colocados são: ')

for pos in colc[20:15:-1]:
    if (pos == colc[16]):
        print(f'{pos}', end = '')
    else:
        print(f'{pos} → ', end = '')

print('\n')

print(f'A tabela em ordem alfabética é: {sorted(colc)}')

print('\n')

print(f'A posição do time da Chapecoense é: {colc.index('Chapecoense') + 1}')