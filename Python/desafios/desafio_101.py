from datetime import date

def voto(ano):
    if idade < 16:
        return 'VOTO NEGADO'
    elif ( (16 <= idade < 18) or (idade > 65) ):
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


while True:

    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano

    print(f'Com {idade} anos: {voto(ano)}')

    resp = input('Quer continuar? [S/N] ').upper()

    if resp == 'N':
        break