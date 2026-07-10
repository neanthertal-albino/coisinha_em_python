from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome = "", sal = 0):
        self.nome = nome
        self._sal = sal

    @property
    def sal(self):
        return self._sal

    @sal.setter
    def sal(self, nsal):
        if nsal >= self._sal:
            self._sal = nsal
        else:
            raise ValueError("NÃO MUDE O SALÁRIO DESSE JEITO!")

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        return f"O manolito {self.nome} tem um salário de {self._sal} sendo um {self.__class__.__name__} e vai ganhar um bonus show de bola de {self.calcular_bonus()}"


class Gerente(Funcionario):
    def __init__(self, n, s):
        super().__init__(n, s)

    def calcular_bonus(self):
        bonus = self._sal * 15 / 100
        return bonus

    

class Designer(Funcionario):
    def __init__(self, n, s):
        super().__init__(n, s)

    def calcular_bonus(self):
        bonus = self._sal * 8 / 100
        return bonus

    

class Desenvolvedor(Funcionario):
    def __init__(self, n, s):
        super().__init__(n, s)

    def calcular_bonus(self):
        bonus = self._sal * 10 / 100
        return bonus

    

    