from rich import inspect, print


class Termostato():

    def __init__(self, t = 16):

        self.temperatura = t
        self.ftemperatura = f'{self.temperatura}°C'
    

a = Termostato()

inspect(a, private=True, methods=True)