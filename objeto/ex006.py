import rich
from rich.panel import Panel
from rich import print
from rich.console import Console
import time

class Caneta:
    contador = 0
    cores = ['red', 'green', 'blue']

    def __init__(self):
        self.tampada = False
        self.cor = Caneta.cores[
                Caneta.contador % len(Caneta.cores)
        ]

    def destampar(self):
        self.tampada = True
    
    def escrever(self, msg=""):
        self.mensagem = msg

        if self.tampada == True:
            print(f'[{self.cor}]{self.mensagem}')

        else:
            print(":sweat_smile: [blue]ops...[/] a [yellow]caneta[/] está [blue]tampada[/]")

    def quebra_linha(self, l=0):
        self.linha = l

        for i in range(self.linha):
            print()

c1 = Caneta()
c1.destampar()
c1.escrever("qualquer coisa")
c1.quebra_linha(2)

c2 = Caneta()
c2.destampar()
c2.escrever("Olá, mundo")
c2.quebra_linha(1)

c3 = Caneta()
c3.destampar()
c3.escrever("Hello, world")
c3.quebra_linha(3)

c4 = Caneta()
c4.destampar()
c4.escrever("Hello, world")
