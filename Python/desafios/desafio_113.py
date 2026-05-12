def leiaInt(msg):
    while True:
        try:
            numInt = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return numInt
        
def leiaFloat(msg):
    while True:
        try:
            numFloat = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: Por Favor, Digite um Número Real Válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return numFloat
        
numInt = leiaInt('Digite um Inteiro: ')
numFloat = leiaFloat('Digite um Real: ')

print(f'O valor Inteiro digitado foi {numInt} e o Real foi {numFloat}')