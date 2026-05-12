from interface import *
from arquivo import *
from time import sleep

arq = 'BD.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    
    if resp == 1:
        lerArquivo(arq)

    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resp == 3:
        cabeçalho('Saindo do Sistema... Até Logo!')

    else:
        print('\033[0;31mERRO: Digite uma Opção Válida!\033[m')

    sleep(2)