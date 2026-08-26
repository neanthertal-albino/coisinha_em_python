from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, msg:str = "", tipo:str = "aviso", icone:str = ":speech_balloon:"):
        self._mensagem = msg
        self._tipo = tipo
        self.icone = icone

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self.icone} {self._tipo.upper()} {self.icone}", style="#ffffff on #000000", width=50)
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg:str = ""):
        super().__init__(msg, tipo="alerta", icone=":warning:")

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self.icone} {self._tipo.upper()} {self.icone}", style="#000000 on #fffc1b", width=50)
        print(msg)


class Erro(Mensagem):
    def __init__(self, msg=""):
        super().__init__(msg, tipo="erro", icone=":prohibited:")
    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self.icone} {self._tipo.upper()} {self.icone}", style="#000000 on #880000", width=50)
        print(msg)