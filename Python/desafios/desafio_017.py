from math import sqrt, hypot

catOpo = float(input('Qual a medida do Cateto Oposto? '))
catAdj = float(input('Qual a medida do Cateto Adjacente? '))

hip = sqrt(catOpo ** 2 + catAdj ** 2)
hip2 = hypot(catOpo, catAdj)

print(f'A hipotenusa do triângulo com Cateto Oposto {catOpo}cm e Cateto Adjacente {catAdj}cm vale {hip:.2f}cm')
print(f'A hipotenusa do triângulo com Cateto Oposto {catOpo}cm e Cateto Adjacente {catAdj}cm vale {hip2:.2f}cm')