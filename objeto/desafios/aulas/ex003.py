from rich import inspect

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
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE.")
        else:
            self.saldo -= valor
            print(f"O saque de R${valor:,.2F} feito pela conta {self.id} efetuado com sucesso")

c1 = ContaBanco(id= 142, nome = "Cleiton", saldo = 5500)
c1.depositar(500)
c1.sacar(2_000)
print(c1)
inspect(ContaBanco)