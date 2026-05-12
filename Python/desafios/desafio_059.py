soma = 0
mult = 0
maior = 0

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))

print(f'=' * 25)
print(f'[1]: Somar')
print(f'[2]: Multiplicar')
print(f'[3]: Maior')
print(f'[4]: Novos números')
print(f'[5]: Sair do programa')
print(f'=' * 25)

opcao = 0

while (opcao != 5):
    opcao = int(input('Escolha uma opção: '))

    if (opcao < 1 or opcao > 5):
        print(f'As opções vão de 1 a 5. Escolha novamente: ')

    if (opcao == 1):
        soma = num1 + num2
        print(f'O valor da soma entre {num1:.2f} e {num2:.2f} é: {soma:.2f}')

    if (opcao == 2):
        mult = num1 * num2
        print(f'O valor da multiplicação entre {num1:.2f} e {num2:.2f} é: {mult:.2f}')

    if (opcao == 3):
        if (num1 > num2):
            maior = num1
            print(f'O maior número é: {maior:.2f}')
            print(f'E o menor número é: {num2:.2f}')
        elif (num1 < num2):
            maior = num2
            print(f'O maior número é: {maior:.2f}')
            print(f'E o menor número é: {num1:.2f}')
        else:
            print(f'Os números são iguais')

    if (opcao == 4):
        num1 = float((input('Digite outro número novamente: ')))
        num2 = float((input('Digite outro número novamente: ')))

    if (opcao == 5):
        print(f'Programa encerrado!')