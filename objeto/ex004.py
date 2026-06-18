from rich import print
import rich.emoji
from rich.table import Table
from rich import box

'''
# Classe de funcionario

class funcionario:
    def __init__(self, n="[ ]", c="[ ]", s="[]", e="[]"):
        self.nome = n
        self.cargo = c
        self.setor = s
        self.empresa = e

        print("  ")
        print(f":handshake: Olá, Meu nome é [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}.")
        print("  ")
    
h1 = funcionario(n="Jailson", c="Guarda", s="Segurança", e="CursoemVideo")
'''
'''
def etiqueta(produto):
    tab = Table(
        title="Produto",
        show_lines=True,
        box=box.ROUNDED
        )

    tab.add_column(produto.nome, justify="center", style="green")
    tab.add_row(f"R$ {produto.preco:,.2f}")

    return tab

class produto:
    def __init__(self, n="<NoNamed>", p=0):
        self.nome = n
        self.preco = p

p1 = produto(n="Petróleo", p=1_000_000.76)
p2 = produto(n="Cavalo", p=1_599.99)

print(etiqueta(p1))
print(etiqueta(p2))
'''
'''
consumo por pessoa = 400g
preço: 82,40/kg
'''

from rich.console import Console
from rich.panel import Panel

console = Console()

class Analisar:
    def __init__(self, pessoas=0):
        self.pessoas = pessoas
        self.kg = pessoas * 0.4
        self.preco = self.kg * 82.40

    def exibir(self):
        texto = (
            f"Para cada pessoa são necessários 0,4 kg de carne.\n\n"
            f"Quantidade de pessoas: {self.pessoas}\n"
            f"Total de carne necessária: {self.kg:.1f} kg\n"
            f"Preço total: R$ {self.preco:.2f}"
        )

        console.print(Panel(texto, title="Relatório do Churrasco"))

c1 = Analisar(100)
c1.exibir()