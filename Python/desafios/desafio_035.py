c1 = int(input('Qual o lado do triângulo? '))
c2 = int(input('Qual o lado do triângulo? '))
c3 = int(input('Qual o lado do triângulo? '))

if(c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1):
    print(f'Os lados {c1}, {c2} e {c3} podem formar um triângulo')
else:
    print(f'Os lados {c1}, {c2} e {c3} não podem formar um triângulo')