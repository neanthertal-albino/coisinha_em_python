class Diario():
    def __init__(self,senha='Cev!@'):
        self.__segredo = []
        self.__senha = senha.strip()

        
    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredo.append(msg.strip())


    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError(f'Senha incorreta! não pode ver meu diário')
        else:
            print(f'Diario liberado.')
            for segredo in self.__segredo:
                print(f'- {segredo}')

    @property
    def senha(senha):
        raise PermissionError(f'Ninguém pode ver.')