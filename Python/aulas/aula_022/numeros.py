from aulas.aula_022.uteis import calculos

num = int(input('Digite um número: '))
fat = calculos.fatorial(num)
print(f'O fatorial de {num} é {fat}.')

print(f'O dobro de {num} é {calculos.dobro(num)}')
print(f'O triplo de {num} é {calculos.triplo(num)}')

