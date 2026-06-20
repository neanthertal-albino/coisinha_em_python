from rich import print
import rich.emoji
from rich.table import Table
import time


'''
# Classe de funcionario

class funcionario:
    empresa = "Curso em Vídeo"
    def __init__(self, n="[ ]", c="[ ]", s="[]"):
        self.nome = n
        self.cargo = c
        self.setor = s

    def apresentar(self):
        print("  ")
        return f":handshake: Olá, Meu nome é [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da {funcionario.empresa}."
        print("  ")
    
h1 = funcionario(n="Jailson", c="Guarda", s="Segurança")
print(h1.apresentar())


class produto:
    def __init__(self, n="<NoNamed>", p=0):
        self.nome = n
        self.preco = p
    
    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += '-' * 30
        precof = f'{self.preco:,.2f}'
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title='produto', width=34)
        print(etiqueta)

p1 = produto(n="Petróleo", p=1_000_000.76)
p2 = produto(n="Cavalo", p=1_599.99)

p1.etiqueta()
p2.etiqueta()
'''
'''
consumo por pessoa = 400g
preço: 82,40/kg
'''
'''
from rich.panel import Panel

class Analisar:
    def __init__(self, titulo, pessoas=0):
        self.titulo = titulo
        self.pessoas = pessoas

        self.kg = pessoas * 0.4
        self.preco = self.kg * 82.40

        self.preco_individual = (
            self.preco / pessoas if pessoas > 0 else 0
        )

    def anali(self):
        conteudo = (
            f"{self.titulo} terá {self.pessoas} participantes.\n"
            f"Cada pessoa comerá 0.4Kg e cada Kg custa 82.40\n"
            f"Recomendo comprar {self.kg:.2f}Kg de carne.\n"
            f"Cada pessoa pagará R$ {self.preco_individual:.2f}"
        )

        painel = Panel(conteudo, title=self.titulo)
        return painel

c1 = Analisar("Churras", 15)
print(c1.anali())
'''

class livro:
    '''
    Uma classe que simula a passagem de páginas;
        pga = página atual
        pgl = páginas lidas em uma sessão
        pt = páginas totais do livro
    '''
    def __init__(self, pga=1, pgl=0, pt=0):
        self.pga = 1
        self.pgl = pgl
        self.pt = pt
    
    def contar(self):
        while self.pga < self.pt:
            print('--'*10)
            print(f"Página atual {self.pga}\nPáginas lidas {self.pgl}\nTotal de páginas {self.pt}\nFaltam {self.pt - self.pga} páginas.")
            print('--'*10)
            self.pgl = int(input("Meu mano, leu quantas paginas ae: "))
            
            if self.pgl < 0:
                print(f':fire: [red]CARA[/], COMO QUE VOCÊ [yellow]LEU[/] PÁGINAS [red]NEGATIVAS[/] AKAKAKAKAK')
                continue

            for p in range(self.pgl):
                self.pga += 1
                print('--'*10)
                time.sleep(0.4)
                print(f'[blue]Leu[/] Página {self.pga}...')
                time.sleep(0.4)
                print('--'*10)
                

                if self.pga >= self.pt:
                    print('\n:book: Opa, você [yellow]terminou[/] o livro.\n')
                    break
            
            
l1 = livro(pga=1, pgl=0, pt=15)
l1.contar()