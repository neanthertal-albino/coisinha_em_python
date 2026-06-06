def aumentar(n, pa, s=False):
    res = n + (n * pa / 100)
    return f'R${res:.2f}' if s else res


def metade(n, s=False):
    res = n / 2
    return f'R${res:.2f}' if s else res
    

def dobro(n, s=False):
    res = n * 2
    return f'R${res:.2f}' if s else res


def red13(n, pd, s=False):
    res = n - (n * pd / 100)
    return f'R${res:.2f}' if s else res 


def moeda(n, s=False):
    return f'R${n:.2f}' if s else n


def resumo(n, pa, pd, s=False):
    print('--'*10)
    print(f'{"Resumo Do Valor":^20}')
    print('--'*10)
    print(f'Preço analisado: R${n:.2f}')
    print(f'O dobro é {dobro(n, s=True)}')
    print(f'A metade do preço é {metade(n, s=True)}')
    print(f'{pa}% de aumento: {aumentar(n, pa, s=True)}')
    print(f'{pd}% de diminuição: {red13(n, pd, s=True)}')
    print('--'*10)