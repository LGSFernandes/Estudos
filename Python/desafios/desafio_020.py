import random

nome1 = input('Qual nome do aluno? ')
nome2 = input('Qual nome do aluno? ')
nome3 = input('Qual nome do aluno? ')
nome4 = input('Qual nome do aluno? ')

lista = [nome1, nome2, nome3, nome4]

ordem = random.shuffle(lista)

print(f'A ordem escolhida foi:')
print(f'{lista}')