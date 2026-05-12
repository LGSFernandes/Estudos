from datetime import date

nasc = int(input('Em que ano você nasceu? '))
hoje = date.today().year
idade = hoje - nasc

if (idade <= 9):
    print(f'Mirim')
elif (idade > 9 and idade <= 14):
    print(f'Infantil')
elif (idade > 14 and idade <= 19):
    print(f'Júnior')
elif (idade == 20):
    print(f'Sênior')
else:
    print(f'Master')