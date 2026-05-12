from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick, jogos=None):
        self.nome = nome
        self.nick = nick
        self.jogos = jogos if jogos else []

    def add_favoritos(self, novo_jogo):
        self.jogos.append(novo_jogo)
        self.jogos.sort()

    def ficha(self):
        if self.jogos:
            lista_formatada = "\n".join([f"🎮 [cyan]{jogo}[/]" for jogo in self.jogos])
        else:
            lista_formatada = "[red]Nenhum jogo favorito[/]"

        conteudo = f"Nome Real: [black on blue] {self.nome} [/]\n\nJogos favoritos:\n{lista_formatada}"

        ficha_tecnica = Panel(
            conteudo,
            title=f"Jogador: <{self.nick}>",
            border_style="blue",
            width=50,
            padding=(1, 2)
        )
        
        print(ficha_tecnica)

j1 = Gamer('Luckas', 'HunteR', ['Fortnite', 'God of War', 'Mario Bros.', 'Sonic'])
j1.ficha()