from rich import print
from rich.table import Table
from rich import inspect

tabela = Table(title="OLÁ")

tabela.add_column(header="Nome", justify="right", style="red")
tabela.add_column(header="GOAT", justify="right", style="blue")

print(tabela)
inspect(print, all=True)