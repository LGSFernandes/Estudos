nome = input('Digite seu nome completo: ')

print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print(f'Seu nome com letras minúsculas: {nome.lower()}')

espacos = nome.replace(' ', '')
quant = len(espacos)

print(f'Quantidade de letras do seu nome (desconsiderando os espaços): {quant}')

primeiro = nome.split()
letras = len(primeiro[0])

print(f'Essa é a quantidade de letras do primeiro nome: {letras}')