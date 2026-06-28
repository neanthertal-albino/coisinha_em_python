from rich import print

class Personagem():
    def __init__(self, N):
        self.nome = N
        self.__hp = 0
        self.__ps = 0
        self.__dict_atributo = {
                'Força': 0,
                'Agilidade': 0,
                'Intelecto': 0
            }

        while True:
            e = False
            for atributo in self.__dict_atributo:
                try:
                    valor = int(input(f'Digite um valor (min: 0/ max: 6/ tot: 12) para atributo de {self.nome}: {atributo} \n'))

                    if 0 <= valor <= 6:
                        self.__dict_atributo[atributo] = valor

                        if self.total() > 12:
                            e = True
                            break
                    else:
                        e = True
                        break

                except ValueError:
                    print('Digite apenas [yellow]números.[/]')
                    e = True
                    break
                
            if not e:
                for nome, valor in self.__dict_atributo.items():
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
                    self.__hp = 25 + (5 * self.__dict_atributo["Força"])
                    self.__ps = 25 + (5 * self.__dict_atributo["Intelecto"])
                    break
            else:
                print('\n[red]ERRO![/] [yellow]VALORES INVÁLIDOS INSERIDOS[/], POR FAVOR [green]INSIRA[/] NOVAMENTE. \n')


    def mostrar(self):
        print(f"[yellow on black]{self.nome}:[/]")
        for nome, valor in self.__dict_atributo.items():
            print(f'[blue on black]----{nome}:[/] {valor}')
        print(f'[blue on black]----HP:[/] {self.__hp}')
        print(f'[blue on black]----PS:[/] {self.__ps}')

    def total(self):
        return sum(self.__dict_atributo.values())


a = False
while True:
    nome = input('Insira o nome do seu personagem:  ').strip()
    if not nome:
        print('[red]ERRO![/] VOCÊ NÃO DIGITOU [yellow]NADA![/]')
    else:
        print('[white on red]ATENÇÃO![/] APÓS ISSO O [yellow on black]NOME[/] JAMAIS, NUNCA E EM NENHUMA HIPÓTESE [red]PODERÁ SER MUDADO[/]')
        a = input("VOCÊ TEM CERTEZA? [S/N] ").strip().lower()
        if a == "s":
            break
        elif a == "n":
            break
        else:
            print("Digite apenas S ou N.")

j1 = Personagem(nome)
j1.mostrar()
