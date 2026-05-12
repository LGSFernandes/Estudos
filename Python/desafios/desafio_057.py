sexo = ''

while (sexo not in ['F', 'M']):
    sexo = str(input('Qual seu gênero (F/M)? ')).upper()

if (sexo == 'F'):
    print(f'Seu gênero é Feminino')
else:
    print(f'Seu gênero é Masculino')