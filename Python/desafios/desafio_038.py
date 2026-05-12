num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

if (num1 > num2):
    print(f'O {num1} é maior que o {num2}')
elif (num2 > num1):
    print(f'O {num2} é maior que o {num1}')
else:
    print(f'Não existe valor maior. Os dois são iguais')