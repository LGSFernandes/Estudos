ext = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 
       'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE'
       'DEZOITO', 'DEZENOVE', 'VINTE')

num = int(input('Digite um número de 0 a 20: '))

while (num < 0 or num > 20):
    if (num < 0 or num > 20):
        print(f'Tente novamente. ', end = '')
        num = int(input('Digite um número de 0 a 20: '))

print(f'O número {num} em extenso é: {ext[num]}')

print('FIM!!!')
