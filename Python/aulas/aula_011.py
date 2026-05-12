print('\033[1;31;43mTeste\033[m')
print('\033[4;30;45mTeste\033[m')
print('\033[7;33;44mTeste\033[m')

a = 3
b = 5

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')

nome = 'Luckas'

cores = {
         'limpa': '\033[m', 
         'azul': '\033[34m', 
         'amarelo': '\033[33m', 
         'pretoebranco': '\033[7m'
        }

print(f'Olá! Muito prazer te conhecer, {cores['pretoebranco']}{nome}{cores['limpa']}! ')
