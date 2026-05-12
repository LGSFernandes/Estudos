from rich import print, inspect

class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    
    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez sua matrícula.')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    
    def dar_aula(self):
        print(f'O Prof. {self.nome} está dando aula.')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor


    def bater_ponto(self):
        print(f'Funcionário {self.nome} bateu o ponto.')


a1 = Aluno('Luckas', 20, 'CC', 'Python')
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods = True)

p1 = Professor('Guanabara', 48, 'Tecnologia', 'Mestre')
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods = True)

f1 = Funcionario('Cleide', 35, 'Secretária', 'Administrativo')
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods = True)
