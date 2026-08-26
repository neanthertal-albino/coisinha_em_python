from model import *
from rich import print

def main():
    p1 = Produto(nome="ouro", preco=4000)
    p2 = Produto(nome='minecraft 2', preco=233)
    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p2
    c2 = c2 + c1


    print(c2)

if __name__ == "__main__":
    main()