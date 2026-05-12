import os
from interface import cabeçalho
    
def arquivoExiste(nome):

    try:
        os.chdir(r"C:\Users\Cliente\Documents\Python\desafios\desafio_115\lib")
        abrir = open(nome, "rt")
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um Erro na Criação do Arquivo!')
    else:
        print(f'Arquivo {nome} criado com Sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao ler o Arquivo {nome}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um Erro na Abertura do Arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um Erro na Hora de Escrever os Dados!')
        else:
            print(f'Novo Registro de {nome} adicionado!')
            a.close()