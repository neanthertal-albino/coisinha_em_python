from abc import ABC, abstractmethod


class Pagamento(ABC):

    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("Valor inválido!")

    @property
    def fvalor(self):
        valor_str = f"{self._valor:,.2f}"
        valor_str = valor_str.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {valor_str}"

    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f'O PAGAMENTO DE {self.fvalor} VIA BOLETO FOI EFETUADO COM SUCESSO'
        except ValueError:
            return f"FALHA NO PAGAMENTO: valor inválido ({valor}) VIA BOLETO!"


class Pix(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f'O PAGAMENTO DE {self.fvalor} VIA PIX FOI EFETUADO COM SUCESSO'
        except ValueError:
            return f"FALHA NO PAGAMENTO: valor inválido ({valor}) VIA PIX!"


def finalizar_compra(tipo_pag: Pagamento, valor):
    print(tipo_pag.pagar(valor))