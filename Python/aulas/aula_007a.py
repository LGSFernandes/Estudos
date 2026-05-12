nome = input('Qual seu nome? ')

print(f'Prazer em te conhecer, {nome:20}!\n') # Com 20 caractéres
print(f'Prazer em te conhecer, {nome:<20}!\n') # Com 20 caractéres alinhado à esquerda
print(f'Prazer em te conhecer, {nome:>20}!\n') # Com 20 caractéres alinhado à direita
print(f'Prazer em te conhecer, {nome:=^20}!\n') # Com 20 caractéres alinhado ao meio e com "=" em volta

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
divint = num1 // num2
exp = num1 ** num2

print(f'A soma, substração e divisão, respectivamente, de {num1} e {num2} são: {soma}, {sub} e {div:.3f}!\n') # Formatado para apenas 3 casas decimais
print(f'A divisão inteira e exponenciação de {num1} e {num2}, respectivamente, são: {divint} e {exp}', end='  ') # Para não quebrar linha 

print(f'AAAAA')