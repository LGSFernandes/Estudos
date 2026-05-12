# Declaração de Classe
class Gafanhoto:

    """
    Essa Classe cria um Gafanhoto.
    Use <variável> = Gafanhoto(<nome>, <idade>) para criar um novo Gafanhoto.
    """

    def __init__(self, nome = '', idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'
    
    def __str__(self):
        return f'Gafanhoto: {self.nome}, Idade: {self.idade}'
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome}; idade = {self.idade}'
        

# Declaração de Objeto
g1 = Gafanhoto('Luckas', 20) # Instanciando um objeto da classe Gafanhoto
print(g1.mensagem())

g2 = Gafanhoto('Anna', 19)
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

print(g1.__doc__) # Mostra a Docstring da Classe, ou seja, a descrição da Classe que foi escrita entre as aspas triplas no início da classe.
print(g1.__dict__) # Mostra em Formato de Dicionário os Atributos do Objeto g1
print(g1.__getstate__())
print(g1.__class__) # Mostra a Classe do Objeto g1, ou seja, a Classe da qual o objeto g1 foi instanciado.

print(g1) # Mostra a Representação em String do Objeto g1, ou seja, o que foi definido no Método __str__ da Classe Gafanhoto. Se o Método __str__ não tivesse sido definido, ele mostraria a representação padrão do objeto, que é algo como <__main__.Gafanhoto object at 0x000001234567890>.