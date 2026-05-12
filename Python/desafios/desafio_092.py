from datetime import datetime

pessoa = dict()

pessoa['nome'] = str(input('Nome: '))

if (type(pessoa['nome']) != str):
    print(f'Formato Inválido. Tente Novamente!')
    pessoa['nome'] = str(input('Nome: '))

pessoa['idade'] = int(input('Ano de Nascimento: '))

if (type(pessoa['idade']) != int):
    print(f'Formato Inválido. Tente Novamente!')
    pessoa['idade'] = int(input('Ano de Nascimento: '))

pessoa['idade'] = datetime.now().year - pessoa['idade']

pessoa['ctps'] = int(input('Carteira de Trabalho (0 para não tem): '))

if (type(pessoa['ctps']) != int):
    print(f'Formato Inválido. Tente Novamente!')
    pessoa['ctps'] = int(input('Carteira de Trabalho (0 para não tem): '))

if (pessoa['ctps'] == 0):
    print('-=' * 20)
    for k, v in pessoa.items():
        print(f'{k} tem o valor de {v}')
    
else:
    pessoa['contratação'] = int(input('Ano de Contratação: '))

    if (type(pessoa['contratação']) != int):
        print(f'Formato Inválido. Tente Novamente!')
        pessoa['contratação'] = int(input('Ano de Contratação: '))

    pessoa['salário'] = float(input('Salário: R$'))

    if (type(pessoa['salário']) != float):
        print(f'Formato Inválido. Tente Novamente!')
        pessoa['salário'] = float(input('Salário: R$'))

    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)

    print('-=' * 20)
    for k, v in pessoa.items():
        print(f'{k} tem o valor de {v}')