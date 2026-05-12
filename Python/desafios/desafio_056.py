maior = 0
mulher = 0
idade_total = 0
nome_homem_mais_velho = ''
maior_idade_homem = 0

for c in range (1, 5):

    print(f'=' * 10, end = '')
    print(f' {c}° Pessoa ', end = '')
    print(f'=' * 10)

    nome = str(input('Qual seu nome? ')).strip()
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual seu gênero? (M/F): ')).strip().upper()

    idade_total += idade

    if (sexo == 'M'):

        if (c == 1): # Se for a primeira pessoa e for homem
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

        elif (idade > maior_idade_homem): # Se for um homem mais velho que o anterior
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    if (idade < 20 and sexo == 'F'):
        mulher += 1

media = idade_total / 4

print(f'A média da idade do grupo é de {media:.2f}')
print(f'O nome do homem mais velho é: {(nome_homem_mais_velho).capitalize()}')
print(f'Tem {mulher} mulheres com menos de 20 anos')