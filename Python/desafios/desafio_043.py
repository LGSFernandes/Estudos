from math import pow

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

denom = pow(altura, 2)

imc = peso / denom

if (imc < 18.5):
    print(f'O IMC é de {imc:.2f} e está abaixo do peso')
elif (imc <= 18.5 and imc < 25):
    print(f'O IMC é de {imc:.2f} e está no peso ideal')
elif (imc <= 25 and imc <= 30):
    print(f'O IMC é de {imc:.2f} e está Sobrepeso')
elif (imc < 30 and imc <= 40):
    print(f'O IMC é de {imc:.2f} e está em Obesidade')
else:
    print(f'O IMC é de {imc:.2f} e está em Obesidade Mórbida')