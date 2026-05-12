pessoas = {
    'nome': 'Luckas',
    'idade': 19,
    'sexo': 'M'
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['nome'] = 'Anna'
pessoas['idade'] = 18

pessoas['peso'] = 50

del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k}: {v}')


estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}

estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}

brasil = list()
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])


estado = dict()
pais = list()

for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))

    pais.append(estado.copy())

for k, v in enumerate(pais):
    print(f'{k}: {v}') 