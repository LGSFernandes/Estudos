from math import sin, cos, tan, radians, sqrt, ceil

ang = float(input('Digite um ângulo: '))

seno = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))

print(f'O Seno, Cosseno e Tangente de {ang} são, respectivamente: {seno:.2f}, {cose:.2f} e {tang:.2f}')

num = 30
raiz = ceil(sqrt(num))
print(f'A raíz de {num} é {raiz}')