import rich
from rich.panel import Panel
from rich import print
from rich.console import Console
import time

console = Console()

class Controle:
    def __init__(self):
        self.turn = False
        self.canal = 1
        self.volume = 1

        while True:
            if self.turn == False:
                console.print(Panel(':heavy_multiplication_x: A TV está [red]desligada[/]!', title="[ TV ]"))
            else:
                console.print(Panel("[blue]Canal[/]  = [black on yellow]1[/] 2 3 4 5\n[blue]Volume[/] = [black on yellow]1[/] 2 3 4 5", title="[ TV ]"))  

            self.control = input("< CH > - VOL + ").strip()
            print("\n"*8)

            if self.control == "0":
                break
                
            if self.control == "@" and self.turn == False:
                self.turn = True
            elif self.control == "@" and self.turn == True:
                self.turn = False


c = Controle()