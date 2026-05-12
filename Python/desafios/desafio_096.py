def area(l, c):
    a = l * c
    return a

print('Controle de Terrenos')
print('-' * 20)

l = float(input('Qual Largura (m)? '))
c = float(input('Qual Comprimento (m)? '))

print(f'A Área do Terreno de Largura {l}m e Comprimento {c}m é de {area(l, c)}m²')