from rich import print
from storage import *

'''
===================================================================
Classe Base de Personagem
===================================================================
'''

class Personagem():
    '''
    Classe Personagem base, define:
    Nome;
    Atributo;
    Classe;
    HP;
    PS;
    '''
    def __init__(self, N):
        self.nome = N
        self.classe = '<Vagabundo>'
        self.__hp = 0
        self.__ps = 0
        self._dict_atributo = {
                'Força': 0,
                'Agilidade': 0,
                'Intelecto': 0
            }


    '''
    ----------------------------------------------------------------------------
    ATRIBUTOS
    ----------------------------------------------------------------------------
    '''
    def calc_atr(self):
        while True:
            error = False
            for atributo in self._dict_atributo:
                try:
                    valor = int(input(f'Digite um valor (min: 0/ max: 8/ tot: 15) para atributo de {self.nome}: {atributo} \n'))

                    if 0 <= valor <= 8:
                        self._dict_atributo[atributo] = valor

                        if self.total() > 15:
                            error = True
                            break
                    else:
                        error = True
                        break

                except ValueError:
                    print('Digite apenas [yellow]números.[/]')
                    error = True
                    break
                
            if not error:
                for nome, valor in self._dict_atributo.items():
                    print(f'    [cyan on black]{nome}:[/] {valor} [cyan]?[/]')

                are_you_sure = input('\nContinuar (isso não poderá ser mudado após a criação do personagem): [SIM/NAO] \n').upper().strip()

                while True:
                    if are_you_sure == 'SIM':
                        break
                    elif are_you_sure == 'NAO':
                        print('Tá bom.')
                        break
                    else:
                        are_you_sure = input('\nAcho que houve um ERRO de digitação (continuar): [SIM/NAO] ').upper().strip()
                
                if are_you_sure == 'SIM':
                    self.calc_hp_ps()
                    break
            else:
                print('\n[red]ERRO![/] [yellow]VALORES INVÁLIDOS INSERIDOS[/], POR FAVOR [green]INSIRA[/] NOVAMENTE. \n')


    '''
    ----------------------------------------------------------------------------
    DISPLAY
    ----------------------------------------------------------------------------
    '''
    def mostrar(self):
        print(f"[yellow on black]{self.nome}:[/]")
        print(f'[black on yellow]{self.classe}:[/]')
        for nome, valor in self._dict_atributo.items():
            print(f'[blue on black]----{nome}:[/] {valor}')
        print(f'[blue on black]----HP:[/] {self.__hp}')
        print(f'[blue on black]----PS:[/] {self.__ps}')



    '''
    ----------------------------------------------------------------------------
    STATUS
    ----------------------------------------------------------------------------
    '''
    def calc_hp_ps(self):
        self.__hp = 25 + (5 * self._dict_atributo["Força"])
        self.__ps = 25 + (5 * self._dict_atributo["Intelecto"])


    
    def total(self):
        return sum(self._dict_atributo.values())


    '''
    ----------------------------------------------------------------------------
    ABSTRATO
    ----------------------------------------------------------------------------
    '''
    def habilidade(self):
        raise NotImplementedError('Essa classe precissa implementar habilidade()')

    
    def to_dict(self):
        return {
            'nome': self.nome,
            'classe': self.classe,
            'atributos': self._dict_atributo,
            'hp': self._Personagem__hp,
            'ps': self._Personagem__ps
        }


'''
============================================================================
CLASSE MAGO
============================================================================
'''
class Mago(Personagem):
    def __init__(self, personagem):
        super().__init__(personagem.nome)
        self._dict_atributo = personagem._dict_atributo.copy()
        self._dict_atributo["Intelecto"] += 3
        self.calc_hp_ps()
        self.classe = '<Mago>'

        self._hability = {
            'Rajada de mana': 5
        }

    
    def habilidade(self):
        return self._hability['Rajada de mana']


'''
============================================================================
CLASSE PALADINO
============================================================================
'''
class Paladino(Personagem):
    def __init__(self, personagem):
        super().__init__(personagem.nome)
        self._dict_atributo = personagem._dict_atributo.copy()
        self._dict_atributo['Força'] += 2
        self.calc_hp_ps()
        self.classe = '<Paladino>'

        self._hability = {
            'Porretada': 4
        }


    def habilidade(self):
        return self._hability["Porretada"]


'''
============================================================================
CLASSE LADINO
============================================================================
'''
class Ladino(Personagem):
    def __init__(self, personagem):
        super().__init__(personagem.nome)
        self._dict_atributo = personagem._dict_atributo.copy()
        self._dict_atributo['Agilidade'] += 4
        self._dict_atributo['Força'] -= 1
        self.calc_hp_ps()
        self.classe = '<Ladino>'

        self._hability = {
            'Esfaquear': 2
        }


    def habilidade(self):
        return self._hability['Esfaquear']


'''
============================================================================
REGISTRO CLASSES
============================================================================
'''
Personagem.CLASSES = {
        0: Mago,
        1: Paladino,
        2: Ladino
    }



'''
============================================================================
SET JOGADORES
============================================================================
'''
def set_jogadores():
    jogadores = []
    
    while True:
        try:
            num_player = int(input('Quantos jogadores [min: 1/max: 5]: '))

            if 1 <= num_player <= 5:
                break
            else:
                print('DIGITE [yellow]APENAS[/] VALORES ENTRE 1 E 5')

        except ValueError:
            print('[red on black]ERRO![/] APENAS VALORES [yellow]NÚMERICOS INTEIROS".[/]')
    

    confirm = ""
    for v in range(num_player):
        while True:
            nome = input(f'Insira o nome do jogador {v + 1}:  ').strip()
            
            if not nome:
                print('[red]ERRO![/] VOCÊ NÃO DIGITOU [yellow]NADA![/]')

            else:
                print('[white on red]ATENÇÃO![/] APÓS ISSO O [yellow on black]NOME[/] JAMAIS, NUNCA E EM NENHUMA HIPÓTESE [red]PODERÁ SER MUDADO[/]')
                confirm = input("VOCÊ TEM CERTEZA? [S/N] ").strip().lower()
                if confirm == "s":
                    base = Personagem(nome)
                    base.calc_atr()

                    print("\nEscolha sua classe:")
                    print("0 = Mago")
                    print("1 = Paladino")
                    print("2 = Ladino")

                    escolha = int(input("> "))

                    jogador = Personagem.CLASSES[escolha](base)

                    jogadores.append(jogador)

                    break
                elif confirm == "n":
                    continue
                else:
                    print("Digite apenas S ou N.")

            
    for j, jogador in enumerate(jogadores, start=1):
            print(f'\nJogador {j} = {jogador.nome}')
            jogador.mostrar()

    return jogadores    
    

set_jogadores()
