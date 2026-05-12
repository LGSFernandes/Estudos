num = int((input('Escolha um número qualquer: ')))
base = str(input('Escolha uma base entre Binário, Octal ou Hexadecimal: ')).upper()

binario = str(bin(num))
octal = str(oct(num))
hexadecimal = str(hex(num))

if (base == 'BINÁRIO'):
    print(f'O número {num} em binário é: {binario[2:]}')
elif (base == 'OCTAL'):
    print(f'O número {num} em Octal é {octal[2:].upper()}')
else:
    print(f'O número {num} em Hexadecimal é {hexadecimal[2:].upper()}')