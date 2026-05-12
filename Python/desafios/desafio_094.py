pessoas = dict()
grupo = list()
soma_idade = 0

while True:
    pessoas['nome'] = str(input('Nome: '))
    
    while True:
        pessoas['sexo'] = str(input('Sexo (F/M): ')).upper().strip()[0]
        if pessoas['sexo'] in 'FM':
            break
        print('ERRO! Responda apenas F ou M.')

    pessoas['idade'] = int(input('Idade: '))
    soma_idade += pessoas['idade']
    
    grupo.append(pessoas.copy())

    while True:
        resp = str(input('Deseja Continuar (S/N)? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
        
    if resp == 'N':
        break

media = soma_idade / len(grupo)

print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')

print(f'C) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print(f'D) Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')