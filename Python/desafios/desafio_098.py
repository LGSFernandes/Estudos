import time

def linhas():
    print('-=' * 20)

def contador(i, f, p):

    if p < 0:
        p = abs(p)
    if p == 0:
        p = 1
        
    linhas()
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    time.sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.3)
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

linhas()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)