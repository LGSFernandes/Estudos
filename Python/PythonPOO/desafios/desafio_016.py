from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f'Este é o funcionário [blue]{self.nome}[/], trabalha no setor de {self.setor} e ocupa o cargo de {self.cargo}.')


f1 = Funcionario('Luckas', 'TI', 'Back-End Developer')
f1.apresentar()