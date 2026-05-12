nome = str(input('Digite seu nome completo: ')).strip()

separado = nome.split()

print(f'Primeiro nome: {separado[0]}')
print(f'Último nome: {separado[len(separado) - 1]}')