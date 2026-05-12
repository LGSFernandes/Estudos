from datetime import date


nasc = int(input('Em que ano você nasceu? '))

hoje = date.today().year

idade = hoje - nasc

data = 18 - idade

if (idade < 18):
    print(f'Ainda irá se apresentar')
    print(f'Ainda faltam {data} anos para você se apresentar')
elif (idade == 18):
    print(f'Está na hora exata de você se apresentar')
else:
    print(f'Já passou da hora de você se apresentar')
    print(f'Já se passaram {abs(data)} de você se apresentar')