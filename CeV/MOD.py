'''
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num=int(input('INSIRA O NÚMERO PRA FATORIAL: '))
fat = fatorial(num)
print(f'O FATORIAL DE {num} É {fat}')

#moeda part1

import moeda

n = float(input('Digite um numero: '))
print(f'A metade de {n} é {moeda.metade(n)}\nO dobro de {n} é {moeda.dobro(n)}\nAumentar 10% de {n} é igual a {moeda.aumentar(n)}\nReduzir 13% de {n} é igual a {moeda.red13(n)}')

#moeda part2

import moeda

n = float(input('Digite um numero: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}\nO dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}\nAumentar 10% de {moeda.moeda(n)} é igual a {moeda.moeda(moeda.aumentar(n))}\nReduzir 13% de {moeda.moeda(n)} é igual a {moeda.moeda(moeda.red13(n))}')

#moeda part3

import moeda

n = float(input('Digite um numero: '))
print(f'A metade de {moeda.moeda(n, s=True)} é {moeda.metade(n, s=True)}\nO dobro de {moeda.moeda(n, s=True)} é {moeda.dobro(n, s=True)}\nAumentar 10% de {moeda.moeda(n, s=True)} é igual a {moeda.aumentar(n, s=True)}\nReduzir 13% de {moeda.moeda(n, s=True)} é igual a {moeda.red13(n, s=True)}')

# Moeda part4'''

import moeda, dado

preco = dado.ler_dinheiro('Digite o preço: ')
pa = int(input('Ola meu cria, quao porcento pa aumenta ae rs: '))
pd = int(input('Ola meu nobre, o porcento de diminuir é quanto kk: '))

moeda.resumo(preco, pa, pd)
