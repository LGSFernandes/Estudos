c1 = float(input('Qual o tamanho do primeiro lado do triângulo? '))
c2 = float(input('Qual o tamanho do segundo lado do triângulo? '))
c3 = float(input('Qual o tamanho do terceiro lado do triângulo? '))

if (c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2):
    print(f'Os lados {c1:.2f}cm, {c2:.2f}cm e {c3:.2f}cm podem formar um triângulo')
    if (c1 == c2 and c1 == c3 and c2 == c3):
        print(f'E é um triângulo equilátero')
    elif (c1 == c2 or c1 == c3 or c2 == c3):
        print(f'E é um triângulo isósceles')
    else:
        print(f'E é um triângulo escaleno')
    
else:
    print(f'Os lados {c1:.2f}cm, {c2:.2f}cm e {c3:.2f}cm não podem formar um triângulo')