from abc import ABC, abstractmethod

class Bebida_quent(ABC):
    def preparar(self):
        print('--INICIANDO O PREPARO--')
        self.ferveragua()
        self.misturar()
        self.servir()
        print('--BEBIDA PRONTA--\n')

    def ferveragua(self):
        print('1. Fervendo água a 100 graus celcius')

    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass

class Cafe(Bebida_quent):
    def misturar(self):
        print('2. Passando água pressurizada pelo pó de café moído.')

    def servir(self):
        print('3. Servir o café em xícara pequena.')


class Cha(Bebida_quent):
    def misturar(self):
        print('2. mergulhar o sachê de ervas na água.')

    def servir(self):
        print('3. servir na caneca de porcelana')

class Leite(Bebida_quent):
    def misturar(self):
        print('2. coisar o leite seila')

    def servir(self):
        print('3. servindo na caneca com café')


    