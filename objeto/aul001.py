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
        pass


class Professor(Pessoa):
    def __init__(self,nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = ""
        self.nivel = ""

    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self,nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = ""
        self.setor = ""

    def bater_ponto(self):
        pass


a1 = Aluno(nome = "Roberto", idade = 18, curso = "seila", turma = 'todas!')
print(a1)