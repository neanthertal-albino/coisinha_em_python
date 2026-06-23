from rich import inspect


class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversário(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self,nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def matricula():
        print(f'O aluno {self.nome} se matriculou')


class Professor(Pessoa):
    def __init__(self,nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} da aulas zika')


class Funcionario(Pessoa):
    def __init__(self,nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print('ponto')


a1 = Aluno(nome = "Roberto", idade = 18, curso = "seila", turma = 'todas!')
a1.fazer_aniversário()
a1.matricula()


p1 = Professor(nome = "carlota", idade = 32,especialidade="matematioca", nivel="MESTRADO" )
p1.fazer_aniversário()


f1 = Funcionario(nome = "Diogo", idade = 22,cargo="diretor",setor="administração" )
f1.fazer_aniversário()
