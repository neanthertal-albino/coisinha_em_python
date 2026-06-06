'''
def ler_dinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        
        try:
            return float(entrada)
        except ValueError:
            print(f'ERRO! "{entrada}" não é um valor válido!')


msg = ler_dinheiro('Digite um valor: ')
'''


