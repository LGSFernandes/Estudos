from random import randint

comp = randint(0, 10)

num = 100

tent = 0

while (num != comp):
    num = int(input('Tente adivinhar o número de 0 a 10: '))
    tent += 1

    if (num != comp):
        print('Você errou! Tente novamente')

print(f'Você acertou! O número era {comp}. ', end = '')
print(f'Foram necessárias {tent} tentativas até acertar')