lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    resp = str(input('Deseja continuar (S/N)? ')).upper()

    while (resp not in 'SN'):
        print('Resposta Inválida. Tente novamente')
        resp = str(input('Deseja continuar (S/N)? ')).upper()

    if (resp == 'N'):
        break

print('-=' * 30)

print(f'Foram digitados {len(lista)} números')

print(f'A lista ao contário é: ', end = '')
lista.sort(reverse = True)

print(f'Lista em Ordem Decrescente: ', end = '')
for c in lista:
    if (c < len(lista) + 1):
        print(f'{c}')
    else:
        print(f'{c} → ', end = '')

if 5 in lista:
    print(f'O número 5 está na lista.')
else:
    print(f'O número 5 não foi digitado na lista')