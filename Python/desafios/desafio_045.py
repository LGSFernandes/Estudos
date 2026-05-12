from random import choice

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']

jogador = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).upper()

comp = choice(jogadas)

if (jogador == comp ):
    print(f'Jogador: {jogador} \n Computador: {comp}')
    print(f'EMPATE!')

elif (jogador == 'PEDRA' and comp == 'PAPEL' or jogador == 'TESOURA' and comp == 'PEDRA' or jogador == 'PAPEL' and comp == 'TESOURA'):
    print(f'Jogador: {jogador} \n Computador: {comp}')
    print(f'Computador \033[37mGanha!!!')
else:
    print(f'Jogador: {jogador} \n Computador: {comp}')
    print(f'Jogador \033[37mGanha!!!')