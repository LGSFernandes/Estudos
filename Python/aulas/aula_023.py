try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    
    r = a / b

except (ValueError, TypeError):
    print(f'Infelizmente tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(f'Não é possível dividir por 0!')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'A causa do erro foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte Sempre! Muito Obrigado!')