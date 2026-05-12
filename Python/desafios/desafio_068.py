from random import randint

cont = 0

while True:
    jogador = str(input('Escolha Par ou Impar: ')).upper().strip()
    while jogador not in ['PAR', 'IMPAR']:
        jogador = str(input('Inválido! Escolha Par ou Impar: ')).upper().strip()

    if jogador == 'PAR':
        comp = 'IMPAR'
    else:
        comp = 'PAR'

    jogador_num = int(input('Escolha um número de 0 a 10: '))
    comp_num = randint(0, 10)
    total = jogador_num + comp_num

    resultado = 'PAR' if total % 2 == 0 else 'IMPAR'

    print(f'O computador escolheu: {comp_num}')
    print(f'{jogador_num} + {comp_num} = {total} ({resultado})')

    if jogador == resultado:
        print('Jogador VENCEU!')
        cont += 1
    else:
        print('Jogador PERDEU!')
        break

print(f'FIM DE JOGO! Você venceu {cont} vezes consecutivas.')