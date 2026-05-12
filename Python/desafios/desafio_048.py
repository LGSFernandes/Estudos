soma = 0
contador = 0

for c in range (1, 501):
    if (c % 2 != 0 and c % 3 == 0):
        print(c)
        contador += 1
        soma += c
    
print(f'O valor total da soma de {contador} números foi de: {soma}')