class Poligono:
    def __init__(self, perimetro):
        self.perimetroq = perimetro
        self.raioc = perimetro
        self.areaq = self.perimetroq * self.perimetroq
        self.areac = self.raioc ** 2 * 3.14
    
    def quadrado(self):
        return f'O Perímetro é {self.perimetroq}\nE a área é {self.areaq}'
    
    def circulo(self):
        return f'O raio é {self.raioc}\nE a área é {self.areac}'


