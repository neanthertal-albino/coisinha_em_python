import rich
from rich import print
from time import sleep
from rich.panel import Panel
from rich.console import Console

console = Console()

class Jogador:
    def __init__(self, nome="<SEM_NOME>", nick="<SEM_NICK>", *jogo):
        self.nome = nome
        self.nick = nick
        self.jogo = list(jogo)

    def Show(self):
        t = (f'{self.nome}\nJogos Favoritos\n\n')

        tg = ""

        self.jogo.sort(key=str.lower)

        for jogo in self.jogo:
            tg += f'- {jogo}\n'

        console.print(Panel(t + tg, title=f'{self.nick}'))

    
j1 = Jogador("Judas", "Macronutrientes", "minecraft", 'hihihiha', "joguinho de bater", "analfabetoland")
j1.Show()

