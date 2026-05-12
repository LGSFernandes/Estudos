maior_de_idade = 0
homem = 0
mulher_menos_20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo? ')).upper().strip()

    resp = str(input('Deseja continuar (S/N)? ')).upper().strip()

    if (resp == 'N'):
        break
    else:
        
        if (idade >= 18):
            maior_de_idade += 1

        if (sexo == 'M'):
            homem += 1
        
        if (sexo == 'F' and idade < 20):
            mulher_menos_20 += 1

print(f'Existem {maior_de_idade} maiores de idade')
print(f'Existem {homem} homens')
print(f'Existem {mulher_menos_20} mulheres abaixo de 20 anos')