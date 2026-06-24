from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, lado):
        self.qtd_lado = lado
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def raio(self):
        pass
        

class Quadrado(Poligono):

    def __init__(self, lados = 1):
        super().__init__(4)
        self.lado = lados

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2

    def raio(self):
        return None


class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * self.raio ** 2

    def raio(self):
        return None