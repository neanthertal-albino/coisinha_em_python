class ContaBancaria():
    def __init__(self):
        self.__saldo = 0
    
    @property
    def saldo(self):
        return self.__saldo


    def depositar(self, valor):
        if valor < 0:
            raise ValueError(f'Valores negativos são inválidos')
        else:
            self.__saldo += valor

        
    def sacar(self, valor):
        if 0 < valor != 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                raise ValueError(f'Não é possível sacar valores maiores que o seu saldo atual.')
        else:
            raise ValueError(f'Não faz sentido sacar valores = 0 ou menores a 0')

