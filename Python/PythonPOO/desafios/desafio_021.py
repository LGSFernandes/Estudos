from rich import print

class Caneta:
    def __init__(self, cor, tampada = True):
        self.cor = cor
        self.tampada = tampada


    def tampar(self):
        self.tampada = True

        if self.tampada:
            print(f'A caneta {self.cor} foi tampada.')


    def destampar(self):
        self.tampada = False

        if not self.tampada:
            print(f'A caneta {self.cor} foi destampada.')


    def escrever(self, texto):
        if self.tampada:
            print(f'A caneta está tampada. Não é possível escrever.')
        else:

            if self.cor == 'preta':
                print(f'Escrevendo com a caneta {self.cor}: [black]{texto}[/]')
                self.tampar()

            elif self.cor == 'vermelha':
                print(f'Escrevendo com a caneta {self.cor}: [red]{texto}[/]')
                self.tampar()

            elif self.cor == 'azul':
                print(f'Escrevendo com a caneta {self.cor}: [bold blue]{texto}[/]')
                self.tampar()


c1 = Caneta('preta')
c2 = Caneta('vermelha')
c3 = Caneta('azul')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, mundo!')
c2.escrever('Python é incrível!')
c3.escrever('Vamos aprender POO!')