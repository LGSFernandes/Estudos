class ContaBancaria:
    """
    Cria uma Conta Bancária que permite fazer Saques e Depósitos.
    """

    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso para {self.titular} com saldo inicial de R${self.saldo:,.2f}.')


    def __str__(self):
        return f'A conta {self.id} pertence a {self.titular} e tem saldo de R${self.saldo:,.2f}.'
    

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')


    def saque(self, valor):
        if valor > self.saldo:
            print(f'Saldo insuficiente para saque de R${valor:,.2f} na conta {self.id}. Saldo atual: R${self.saldo:,.2f}')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')

c1 = ContaBancaria(1, 'Luckas', 15000)
c1.deposito(500)
c1.saque(2_000_000)
print(c1)