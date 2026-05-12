from rich import print
from rich.panel import Panel
from time import sleep

class Livro:
    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.pagina_atual = 0
        self.lido = False

    def folhear(self, paginas=1):
        if self.lido:
            print(f"[yellow]O livro '{self.titulo}' já foi finalizado![/]")
            return

        print(f"[cyan]Folheando {paginas} página(s)...[/]")
        sleep(0.5)
        self.pagina_atual += paginas

        if self.pagina_atual >= self.total_paginas:
            self.pagina_atual = self.total_paginas
            self.lido = True
            self.status()
        else:
            self.status()

    def status(self):
        progresso = (self.pagina_atual / self.total_paginas) * 100
        
        texto = f"""[bold]{self.titulo}[/] - {self.autor}
Página: [blue]{self.pagina_atual}[/] / [blue]{self.total_paginas}[/]
Progresso: [green]{progresso:.1f}%[/]"""

        if self.lido:
            texto += "\n\n[bold green]Status: LEITURA CONCLUÍDA! 🎉[/]"
        else:
            texto += f"\n\nStatus: Lendo..."

        print(Panel(texto, title="Biblioteca Digital", border_style="magenta", width=50))

meu_livro = Livro("Dinossauros Exóticos", "Luckas", 800)

meu_livro.status()
sleep(1)

meu_livro.folhear(350)
sleep(1)

meu_livro.folhear(450)