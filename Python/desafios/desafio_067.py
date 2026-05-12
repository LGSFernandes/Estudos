while True:

    num = int(input('Digite um número para ver sua tabuada (negativo para parar): '))

    if (num < 0):
        break

    print((f'A tabuada de {num} é:'))
    
    for c in range (0, 11):
        print(f'{c} x {num} = {c * num}')
