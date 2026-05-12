def fatorial(n, show = False):
    f = 1

    for c in range (n, 0, -1):
        if show:
            
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')

        f *= c
    return f

print(fatorial(5, show = True))
print(fatorial(5))