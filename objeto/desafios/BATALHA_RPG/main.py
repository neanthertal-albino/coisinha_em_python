from model import *

def main():
    p1 = Guerreiro('Kratos', 10_000)
    p2 = Mago('Frieren', 4_000)

    p1.atacar(p2, 100)

    p2.curar()
    p2.atacar(p1)

    p1.curar()



if __name__ == "__main__":
    main()