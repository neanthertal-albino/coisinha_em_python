'''# fogo de artifício

import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('YAY!')

#de 1 a 50 em par

for c in range(1, 51):
    if c % 2 == 0:
        print(c)

#impar 3 até 500

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c

print(soma)

#tabuada 2

t = int(input('que numero vc quer tabuadinha?: '))
for c in range(1, 11):
    r = t * c
    print(f'{c} * {t} = {r}')


#sla par somar e é isso

p = 0

for c in range(0, 6):
    n = int(input('digite um numero: '))
    if n % 2 == 0:
        p += n
    
print(p)


#pa

a1 = int(input('selecione o primeiro termo: '))
r = int(input('selecione a razão: '))
decimo = a1 + (10-1) * r

for c in range(a1, decimo + r, r):
    print(a1, '-> ', end='')
    a1 += r
print('Cabo!')

#primos(esse n entendi a logica)


n = int(input('Digite um número: '))
div = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m')
        div += 1
    else:
        print('\033[35m')
    print(c, end=' ')

if div == 2:
    print(f'\033[33mé PRIMO')
else:
    print(f'\033[31mNÃO é PRIMO')
print(f'\033[mJá que {n} foi dividido {div} vezes')

#palindromo

fra = str(input('Escreva uma frase: ')).strip().upper()
pala = fra.split()
junto = ''.join(pala)
inv = ''

for letra in range(len(junto) - 1, -1, -1):
    inv += junto[letra]

print(f'{inv} / {junto}')

if inv == junto:
    print('\033[33mPALÍNDROMO')
else:
    print('\033[31mNÃO É PALÍNDROMO')

#verificador de idades

from datetime import date

atual = date.today().year
me = 0
ma = 0

for c in range(0, 7):
    y = int(input('Ano q vc nasceu '))
    if atual - y < 21:
        me += 1
    else:
        ma += 1

print(f'{me} esses são menores de idade, e {ma} são maiores de idade')

#analisator of pesos
ma = 0
me = 0
for q in range(5):
    p = float(input('quanto vc pesa? '))
    if q == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            p = me
print(f'maior {ma} e menor {me}')

#analisador completo
import datetime

somaidade = 0
maioridademan = 0
nomehomemveio = ''
quantidade_muie = 0

for p in range(1, 5):
    print(f'-------PESSOA NÚMERO {p}---------')
    nome = str(input(f'nome da pessoa: ')).strip()
    sexo = str(input('sexo dessa pessoa [M/F]: ')).upper()
    idade = int(input('Idade dessa pessoa: '))
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridademan = idade
        nomehomemveio = nome
    if sexo == 'M' and maioridademan < idade:
        maioridademan = idade
        nomehomemveio = nome
    if sexo == 'F' and idade < 20:
        quantidade_muie += 1


media = somaidade / 4
print(f'media de idade de todo mundo {media}')
print(f'o nome do HOMEM mais velho é {nomehomemveio} com {maioridademan}')
print(f'a quantidade de mulhieres com a idade menor que 20 anos é {quantidade_muie}')
#'''