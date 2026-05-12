nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))

media = (nota1 + nota2) / 2

if (media < 5):
    print(f'Sua média foi de {media:.2f}. \033[31mREPROVADO\033[m')
elif (media >= 5 and media < 7):
    print(f'Sua média foi de {media:.2f}. \033[33mRECUPERAÇÃO\033[m')
else: 
    print(f'Sua média foi de {media:.2f}. \033[32mAPROVADO\033[m')