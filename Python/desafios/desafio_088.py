from random import randint
from time import sleep

lista_composta = list()
jogo_temporario = list()

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))
total_jogos = 1

while total_jogos <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo_temporario:
            jogo_temporario.append(num)
            cont += 1
        if cont >= 6:
            break
            
    jogo_temporario.sort() 
    lista_composta.append(jogo_temporario[:])
    jogo_temporario.clear() 
    total_jogos += 1

print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '=-' * 3)
for i, l in enumerate(lista_composta):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5) 
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)