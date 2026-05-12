from random import randint

num = randint(0, 5)

chute = int(input('Tente adivinhar o número: '))

if (num == chute):
    print(f'Você acertou, o número era {num}')
else:
    print(f'Você errou, o número era {num}')