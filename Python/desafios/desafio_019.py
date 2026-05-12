import random

nome1 = input('Qual nome do aluno? ')
nome2 = input('Qual nome do aluno? ')
nome3 = input('Qual nome do aluno? ')
nome4 = input('Qual nome do aluno? ')

nomes = [nome1, nome2, nome3, nome4]

escolhido = random.choice(nomes)

print(f'O aluno escolhido foi {escolhido}')