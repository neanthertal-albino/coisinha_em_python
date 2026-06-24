import rich
from rich.panel import Panel
from rich import print
from rich.console import Console
import time

class Caneta:
    def __init__(self, cor):
        self.tampada = False
        match cor.lower().strip():
            case 'azul':
                escolha = 'blue'
            case 'verde':
                escolha = 'green'
            case 'vermelho':
                escolha = 'red'
            case _:
                escolha = 'white'
            
        self.cor = escolha

    def destampar(self):
        self.tampada = True
    
    def escrever(self, msg=""):
        self.mensagem = msg

        if self.tampada == True:
            print(f'[{self.cor}]{self.mensagem}')

        else:
            print(f":sweat_smile: [{self.cor}]ops... a caneta está tampada")

    def quebra_linha(self, l=0):
        self.linha = l

        for i in range(self.linha):
            print()

c1 = Caneta(cor="verde")
c1.destampar()
c1.escrever("qualquer coisa")
c1.quebra_linha(2)

