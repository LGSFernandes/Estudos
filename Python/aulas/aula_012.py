nome = str(input('Qual seu nome? '))
nome = nome.upper()

if (nome == 'LUCKAS' or nome == 'LAURA' or nome == 'ANA'):
    print(f'Que belo nome, {nome.capitalize()}')
elif (nome in 'ANA VITÓRIA PROENÇA COSTA LOPES'):
    print(f'É um belíssimo nome, {nome.capitalize()}')
elif (nome == 'PEDRO' or nome == 'MARIA' or nome == 'FELIPE'):
    print(f'Seu nome é muito comum no Brasil, {nome.capitalize()}')
else:
    print(f'Que nome feio {nome.capitalize()}')
    
print(f'Tenha um bom dia, {nome.capitalize()}')