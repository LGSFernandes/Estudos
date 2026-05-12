aluno  = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Qual foi a média de {aluno["nome"]}? '))

if (aluno['media'] >= 7):
    aluno['situacao'] = '\033[32mAPROVADO!\033[m'
else:
    aluno['situacao'] = '\033[31mREPROVADO!\033[m'

print(f'A situação de {aluno["nome"]} é {aluno["situacao"]}')