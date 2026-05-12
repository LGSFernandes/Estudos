expr = str(input('Digite uma expressão (Que use parênteses): '))
pilha = []

for c in expr:
    if (c == '('):
        pilha.append('(')
    elif (c == ')'):
        if (len(pilha) > 0):
            pilha.pop()
        else:
            pilha.append(')')
            break

if (len(pilha) == 0):
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida')