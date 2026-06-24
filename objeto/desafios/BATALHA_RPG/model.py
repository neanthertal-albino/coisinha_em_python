from abc import ABC, abstractmethod
from rich import inspect, print
from random import randint
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            # COMBATE
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'[yellow]{self.nome}[/]({self.vida}) [red]ATACOU[/] [blue]{alvo.nome}[/]({alvo.vida}) com [blue]{golpe}[/] de dano máximo {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque de {self.nome} a {alvo.nome} não pode acontecer')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu [red]{fator} de DANO[/] (vida atual: {self.vida})')

    @abstractmethod
    def curar(self):
        pass

    def status_perso(self):
        pass
    

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe de machado', 'BREAK UP EVERYTHING!!!']

    def curar(self):
        fator = random.randint(0, 10)
        self.vida += fator
        print(f'[yellow]{self.nome}[/] Utilizou uma pedra da vida e [green]recuperou {fator}[/] de vida (vida atual: {self.vida})')


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Zoltrak', 'FIRE BALL', 'BLACK HOLE']

    def curar(self):
        fator = random.randint(0, 10)
        self.vida += fator
        print(f'[yellow]{self.nome}[/] Utilizou uma magia de cura e [green]recuperou {fator}[/] de vida (vida atual: {self.vida})')