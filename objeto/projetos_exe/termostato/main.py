from model import *
from rich import inspect, print

def main():
    t = Termostato()
    try:
        t.temperatura = 22.3
        print(t.ftemperatura)
    except Exception as e:
        print(f'Houve um problema: {e}')
if __name__ == "__main__":
    main()