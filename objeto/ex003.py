class ContaBanco:
    """
    O ContaBanco cria uma conta bancária com id, nome e saldo.
    """
    def __init__(self, id=000, nome = "SemNome", saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.nome} tem R${self.saldo:.2f} de salario."

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        pass

c1 = ContaBanco(id= 142, nome = "Cleiton", saldo = 5500)
c1 = depositar(500)
print(c1)