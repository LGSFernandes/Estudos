teste = list()

teste.append('Luckas')
teste.append(19)

print(teste)

galera = list()

galera.append(teste[:])
print(galera)

teste[0] = 'Ana'
teste[1] = 18

galera.append(teste[:])
print(galera)


rapaziada = [['Laura', 10], ['Pedro', 3], ['Renan', 16], ['Maria', 15]]
print(rapaziada)

for i, j in rapaziada:
    print(f'{i}, {j}')


grupo = list()
dado = list()
mai = men = 0

for c in range (0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))

    grupo.append(dado[:])

    dado.clear()

print(f'{grupo}\n{dado}')

for c in grupo:
    if (c[1] >= 18):
        print(f'{c[0]} é maior de idade.')
        mai += 1
    else:
        print(f'{c[0]} é menor de idade')
        men += 1

print(f'Tem {mai} maiores de idade e {men} menores de idade')