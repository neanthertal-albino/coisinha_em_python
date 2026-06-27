from abc import ABC
from datetime import date, datetime

class Pessoa():
    def __init__(self, n, i):
        self.nome = n
        self.__idade = i
        
    @property
    def idade(self):
        return self.__idade


class Aluno(Pessoa):
    def __init__(self,n, i, m):
        super().__init__(n, i)
        self.matricula = m

    def mostrar(self):
        return (
            f'Aluno: {self.nome}'
            f'\nIdade: {self.idade}'
            f'\nMatrícula: {self.matricula}'
        )

a = Aluno("carlos", 23, 12345677)
print(a.mostrar())