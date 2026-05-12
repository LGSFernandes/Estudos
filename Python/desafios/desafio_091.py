from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
ranking = list()

for c in range (1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)

print('Valores Sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} tirou o número {v}')
    sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-=' * 15)
print('  == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'   {i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)