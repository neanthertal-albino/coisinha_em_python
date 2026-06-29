from model import Diario
from rich import inspect

def main():
    meudiario = Diario()
    meudiario.escrever("Hello world")

    try:
        meudiario.ler('123')
    except Exception as e:
        print(f"ERRO: {e}")

if __name__ == "__main__":
    main()