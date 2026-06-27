from abc import ABC
from datetime import date, datetime

class Pessoa():
    def __init__(self, n):
        self.nome = n
        self.__idade = 0
        
    @property
    def idade(self):
        pass


a = Pessoa('Carlos')
print(a.ano(2000))