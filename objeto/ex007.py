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
        self.max_vol = 5
        self.min_vol = 0
        self.max_canal = 5
        self.barra = ""
        self.texto_canais = ""

        while True:
            if self.turn == False:
                console.print(Panel(':heavy_multiplication_x: A TV está [red]desligada[/]!', title="[ TV ]"))
            else:
                console.print(Panel(f"[blue]Canal[/]  = {self.texto_canais}\n[blue]Volume[/] = {self.barra}", title="[ TV ]"))  

            self.control = input(f"< CH{self.canal} > - VOL{self.volume} + ").strip()
            print("\n"*10)

            if self.control == "0":
                break

            if self.control == "@" and self.turn == False:
                self.turn = True

            elif self.control == "@" and self.turn == True:
                self.turn = False

            if self.turn == True: 
                if self.control == "+" and self.volume < self.max_vol:
                    self.volume += 1

                elif self.control == '-' and self.volume > self.min_vol:
                    self.volume -= 1


                if self.control == ">":
                    if self.canal == self.max_canal:
                        self.canal = 1
                    else:
                        self.canal += 1
                
                elif self.control == "<":
                    if self.canal == 1:
                        self.canal = self.max_canal
                    else:
                        self.canal -= 1


            self.barra = "█" * self.volume + "░" * (self.max_vol - self.volume)

            self.texto_canais = ""

            for c in range(1, self.max_canal + 1):
                if c == self.canal:
                    self.texto_canais += f"[black on yellow] {c} [/]"
                else:
                    self.texto_canais += f" {c} "




c = Controle()