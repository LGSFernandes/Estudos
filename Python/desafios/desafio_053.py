frase = str(input('Digite uma frase: '))

limpa = "".join(frase.split()).upper()

palin = True

tam = len(limpa)

for c in range (tam // 2):
    if (limpa[c] != limpa[tam - 1 - c]):
        palin = False
        break

if palin:
    print(f'A frase "{frase}" é um Palíndromo')
else:
    print(f'A frase "{frase}" não é um Palíndromo')