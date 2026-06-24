from rich import print, inspect
from model000 import *

def main():
    a1 = Quadrado(20)
    #inspect(a1, methods=True)
    print(f'Um quadrado de {a1.lado} lados tem {a1.perimetro()} mm')
    print(f'E uma área de {a1.area()} mm')

    c = Circulo()
    print(f'Um circulo de raio {c.raio} cm tem perímetro {c.perimetro():,.2f}')
    print(f'E uma area de {c.area():,.2f} cm')

if __name__ == "__main__":
    main()