from model import *

def main():
    c = ContaBancaria()
    print(c.saldo)
    c.depositar(20)
    print(c.saldo)
    c.depositar(500)
    print(c.saldo)
    c.sacar(50)
    print(c.saldo)
    c.sacar(-60)
    print(c.saldo)

if __name__ == "__main__":
    main()