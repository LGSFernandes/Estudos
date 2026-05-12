km = float(input('Qual foi a velocidade do carro? '))

if(km > 80):
    print(f'Foi ultrapassado o limite de velocidade. Você será multado...')

    multa = (km - 80) * 7

    print(f'O valor da multa será de R${multa:.2f}')