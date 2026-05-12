lista = ('Pão', 2.5, 'Caneta', 4, 'Livro', 7, 'Leite', 12, 'Carne', 35, 'Mouse', 76, 
        'Teclado', 350, 'Vinho', 700, 'PC', 5000, 'Carro', 20000, 'Casa', 100000)

print(f'-' * 40)
print(f'           LISTAGEM DE PREÇOS            ')
print(f'-' * 40)

for c in lista:
    
    if (type(c) == str):
        print(f'{c:.<30}', end = '')
    else:
        print(f'R${c:.2f}')

print(f'-' * 40)