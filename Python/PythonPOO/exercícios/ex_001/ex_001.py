# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

# Declaração de Objeto
g1 = Gafanhoto() # Instanciando um objeto da classe Gafanhoto
g1.nome = 'Luckas'
g1.idade = 20
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Anna'
g2.idade = 19
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = 'Laura'
g3.idade = 10
print(g3.mensagem())