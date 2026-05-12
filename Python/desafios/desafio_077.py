lista = ('Visao', 'Cria', 'Ainda', 'NeSegredo', 'PegaVisao', 'EsquecePai', 'TaLigadoNe')

for c in lista:
    vogal = 0
    for i in c:
        if (i.upper() in 'AEIOU'):
            vogal += 1

    if (vogal == 1):
        print(f'A Palvra {c} tem: {vogal} vogal')
    else:
        print(f'A palavra {c} tem: {vogal} vogais')