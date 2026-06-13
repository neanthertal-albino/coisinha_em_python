#   INICIANDO CRIAÇÃO DE CLASSES E OBJETO

class gafanhoto: 
    def __init__(self):
        self.nome = ""
        self.idade = 0
    
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"O {self.nome} é gafanhoto e tem {self.idade} anos de idade."

g1 = gafanhoto()
g1.nome = "Marcos"
g1.idade = 19
print(g1.mensagem())
