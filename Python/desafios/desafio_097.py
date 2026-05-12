def linhas (msg):
    for c in range (0, len(msg)):
        print('~', end='')
    print()

    print(f'{msg}')

    for c in range (0, len(msg)):
        print('~', end='')
    print()


linhas('  Luckas Fernandes  ')
linhas('  Curso em Vídeo  ')
linhas('  CeV  ')