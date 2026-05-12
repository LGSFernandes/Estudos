nome = input('Qual seu nome? ')

if(nome == 'Luckas'):
    print(f'Que belo nome, {nome}!')
else:
    print(f'Que nome comum, {nome}')

print(f'Boa tarde, {nome}')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if(media >= 6):
    print(f'{media:.2f} Está acima da média!')
else:
    print(f'{media:.2f} está abaixo da média')