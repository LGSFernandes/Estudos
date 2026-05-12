def soma(a, b):
    print(f'A soma entre {a} e {b} é {a + b}')
    

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

soma(a, b)

def contador(* num):
    soma = 0
    for c in num:
        soma += c

    print(f'A soma dos números é {soma}')

contador(5, 3, 6, 10, 22, 67, 8)

def dobra(lst):
    pos = 0
    while(pos < len(lst)):
        lst[pos] *= 2
        pos += 1

    print(f'A Lista Dobrada será {lst}')

valores = [7, 2, 5, 0, 4]
dobra(valores)