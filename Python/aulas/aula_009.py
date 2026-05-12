frase = '    Curso em Vídeo Python    '

print(f'Esta é a frase completa: "{frase.strip()}"')
print(f'Esta é a letra do 3° índice "({frase.strip()[3]})" da frase "{frase}"')
print(f'Estas são as letras do 3° índice até o 12° "({frase.strip()[3:13]})" da frase "{frase}"')
print(f'Estas são as letras do início da até o 12° índice "({frase.strip()[:13]})" da frase "{frase}"')
print(f'Estas são as letras do 1° índice até o 15°, pulando 1 "({frase.strip()[1:15:2]})" da frase "{frase}"')
print(f'Estas são as letras do 1° índice até o último, pulando 1 "({frase.strip()[1::2]})" da frase "{frase}"')
print(f'Estas são todas as letras, pulando 1 "({frase.strip()[::2]})" da frase "{frase}"')

print(f'Existem {frase.strip().count('o')} letras "o" na frase "{frase}"')
print(f'Esta é a quantidade de "O" Maiúsculo, após transformar a frase toda em Maiúsculo: {frase.strip().upper().count('O')}')

print(f'Este é o tamanho da frase: {len(frase)} caractéres')

print(f'Este é o tamanho da frase removendo espaços indesejados: {frase.strip()}')
        # Existe lstrip (Remove apenas da esquerda), e rstripe (Remove apenas da direita)

print(f'Esta é a frase trocando "Python" por "Android": {frase.replace('Python', 'Android')}')

print(f'Aqui mostra se a palavra "Curso" está dentro da frase: {'Curso' in frase}')

print(f'Aqui mostra a posição (da primeira letra) da palavra "Curso": {frase.strip().find('Curso')}')

print(f'Aqui mostra a posição (da primeira letra) da palavra "vídeo": {frase.strip().find('vídeo')}')
        # Retornará -1, pois não há "vídeo", mas sim "Vídeo"

print(f'Aqui mostra a posição (da primeira letra) da palavra "vídeo", após transformar tudo em Minúscula: {frase.strip().lower().find('vídeo')}')

dividido = frase.split() # Separa a frase em palavras e cria uma lista nova com essas palavras
print(f'Aqui mostra apenas a primeira palavra da frase: {dividido[0]}')

print(f'Aqui mostra a letra de índice 3 da palavra de índice 2: {dividido [2] [3]}')

print("""\nLorem ipsum dolor sit amet, consectetur
adipiscing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur.""")