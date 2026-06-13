<<<<<<< Updated upstream
#   CONTINUANDO CRIAÇÃO DE CLASSES E OBJETO

class gafanhoto:
    """
    Esta classe cria um Gafanhoto, que é uma pessoa muito zika que gosta de aprender, e essa pessoa tem NOME e IDADE.
    """
=======
#   INICIANDO CRIAÇÃO DE CLASSES E OBJETO

class gafanhoto: 
>>>>>>> Stashed changes
    def __init__(self, n="Vazio", i=0):
        self.nome = n
        self.idade = i
    
    def aniversario(self):
        self.idade = self.idade + 1

<<<<<<< Updated upstream
    def __getstate__(self):
        return f"O {self.nome} é gafanhoto e tem {self.idade} anos de idade."

    def __str__(self):
        return f"O {self.nome} é gafanhoto e tem {self.idade} anos de idade."

g1 = gafanhoto(n = "Marcos", i = 19)
# Eu esqueci de chamar a função de aniversário no outro código.
g1.aniversario()
#print(g1)

# print(g1.__doc__)

print(g1.__dict__) # atributo
print(g1.__getstate__()) # metodo 
print(g1.__class__)
=======
    def mensagem(self):
        return f"O {self.nome} é gafanhoto e tem {self.idade} anos de idade."

g1 = gafanhoto("Marcos", 19)
# Eu esqueci de chamar a função de aniversário no outro código.
g1.aniversario()
print(g1.mensagem())
>>>>>>> Stashed changes
