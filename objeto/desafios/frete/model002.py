from abc import ABC,abstractmethod

class Transporte(ABC):

    def __init__(self, d):
        self.distancia = d
        self.frete = 0

    @abstractmethod
    def cal_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, d):
        super().__init__(d)

    def cal_frete(self):
        self.frete = self.distancia * Moto.fator
        return f'R${self.frete:,.2f}'


class Caminhao(Transporte):
    fator = 1.20
    def cal_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return 'Raio mínimo é 50km'
        else:
            self.frete = self.distancia * Caminhao.fator
            return f'R${self.frete}'

class Drone(Transporte):
    fator = 9.50
    def cal_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return 'Raio máximo é 10km'
        else:
            self.frete = self.distancia * Drone.fator
            return f'R${self.frete}'