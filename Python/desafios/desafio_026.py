frase = str(input('Digite uma frase: ')).upper().strip()

frase = frase.upper()

print(f'A letra "A" aparece: {frase.count('A')} vezes')
print(f'A letra "A" aparece pela primeira vez no índice: {frase.find('A')+1}')
print(f'A letra "A" aparece pela última vez no índice {frase.rfind('A')+1}')