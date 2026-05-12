from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas


    def calcular(self):
        consumo_por_pessoa = 0.4
        preco = 82.40

        valor = self.pessoas * consumo_por_pessoa * preco

        quantidade_carne = self.pessoas * consumo_por_pessoa

        informacao = f"""Analisando o [green]{self.titulo}[/] com [blue]{self.pessoas}[/] pessoas...
Cada participante comerá 0.4k e cada Kg custa R$ 82,40.
Recomendo [blue]comprar {quantidade_carne:.3f}Kg[/] de carne.
O valor total gasto com carne para o churrasco será de [green]R${valor:,.2f}[/].
Dividindo o valor total pelo número de participantes, cada um pagará [orange]R${valor / self.pessoas:,.2f}[/]."""

        cont = Panel(
            informacao,
            title= f'[red]{self.titulo}[/]',
            width=90,
            style='bold white',
            border_style='bright_black'
        )

        print(cont)
    

c1 = Churrasco('Churras dos Querem Nada', 15)
c1.calcular()