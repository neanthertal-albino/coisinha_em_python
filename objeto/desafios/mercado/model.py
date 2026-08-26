class Produto:
    def __init__(self, nome:str, preco:float = 0):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"{self.nome} ({formata_dinheiro(self.preco)})"


class Carrinho:
    def __init__(self, produtos:list = None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        return sum(p.preco for p in self.produtos)

    def __add__(self, other):
        if isinstance(other, Produto):
            return Carrinho(self.produtos + [other])
        elif isinstance(other, Carrinho):
            return Carrinho(self.produtos + other.produtos)
        else:
            raise TypeError("Você ta fazendo besteira")

    def __str__(self):
        linha = "\n" + "-" * 30
        itens = "\n".join(str(p) for p in self.produtos)
        return f'{itens}\n{linha}\nTotal: {formata_dinheiro(self.total)}{linha}'


def formata_dinheiro(valo:float):
    import locale

    locale.setlocale(locale.LC_ALL, locale="pt_BR.UTF-8")
    return locale.currency(valo, grouping=True)