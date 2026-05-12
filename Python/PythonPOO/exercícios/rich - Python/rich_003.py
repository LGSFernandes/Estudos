from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')

tabela.add_column('Nome', justify='center', style='cyan', no_wrap=True)
tabela.add_column('Preço', justify='right', style='green')

tabela.add_row('Coca-Cola', 'R$ 5,00')

print(tabela)