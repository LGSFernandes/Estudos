from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        largura = 40 
        
        linha_nome = f"{self.nome:^36}"
        divisor = f"{'-':-^36}"
        linha_preco = f"{'R$' + f'{self.preco:,.2f}':.^36}"
        
        conteudo = f"{linha_nome}\n{divisor}\n{linha_preco}"
        
        etiqueta_painel = Panel(
            conteudo, 
            title='Produto', 
            width=largura, 
            style='bold white', 
            border_style='bright_black'
        )
        
        print(etiqueta_painel)

# Testando
p1 = Produto('iPhone 17 Pro Max', 25000.85)
p2 = Produto('Notebook Gamer', 8000.00)

p1.etiqueta()
p2.etiqueta()