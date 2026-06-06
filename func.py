#FUNÇÕES YAY
'''#controle de area

def area(l, c):
    a = l * c
    print(f'A area de uma largura de {l} e um comprimento de {c} é {a}')


area(float(input('Qual a largura do terreno?: [m] ')),
float(input('Qual o comprimento do terreno?: [m] ')))

#texto adaptável

def escreva(msg):
    t = len(msg) + 4
    print('-' * t)
    print(f'{msg:^{t}}')
    print('-' * t)


escreva(input('Escreva: '))

#Contador multiversal pika das galaxias v2

import time

def cont(i, f, p):

    if p == 0:
        p = 1
    
    if i > f:
        p = -abs(p)
    else:
        p = abs(p)

    print(f'A CONTAGEM DE {i} até {f} de {abs(p)} em {abs(p)}:')

    for va in range(i, f+ (1 if p > 0 else -1), p):
        print(va, end=' -> ', flush=True)
        time.sleep(1)

    print('FIM!!!')
    print('__'*20)


cont(1, 10, 1)
cont(10, 0, -2)
cont(int(input('ESCOLHA O VALOR INICIAL: ')), int(input('ESCOLHA O VALOR FINAL: ')), int(input('ESCOLHA O VALOR DE INTERVALO: ')))

#função para descobrir o maior e o menor

import time

def maior(*val):
    ma = 0
    for v in val:
        print(f'{v}', end=' ', flush=True)
        time.sleep(1)

    print(f'tem {len(val)} valores')
    for i, v in enumerate(val):
        if i == 0:
            ma = v
        else:
            if v > ma:
                ma = v
    print(f'o maior valor foi {ma}')
    print('__'*30)

maior(1, 3, 2, 7, 3)
maior(3,4,2,2)
maior(0,1)
maior(5)
maior()

#MEU DEUS ISSO NAO ACABA NUNCA (sorteio, mais e pares...)

import random
import time

ns = [random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)]

def sorteio():
    for i in ns:
        print(i, end=' ', flush=True)
        time.sleep(1)

def somapar():
    v = 0
    for i in ns:
        if i % 2 == 0:
            v += i
    print(f'os pares somados dessa bomba resulta em {v}')

sorteio()
somapar()

#outro teste

def somaxx(a=0, b=0, c=0):
    s = a + b + c
    return s

rsp1 = somaxx(1, 3, 5)
rsp2 = somaxx(3, 8)
rsp3 = somaxx(6)
print(rsp1, rsp2, rsp3)

#outra votação

import datetime

def vota(an = 0):
    aa = datetime.date.today().year
    i = aa - an
    return i

    if i < 16:
        print(f'Muito cedo para votar com {i} anos')
    elif i < 18:
        print(f'O voto é opcional com {i} anos')
    elif i < 60:
        print(f'O voto obrigatório com {i}')
    else:
        print(f'O voto é opcional com {i} anos')

i = vota(int(input('Digite o ano em que você nasceu: ')))

#mais um fatorial...

def fatorial(num, show=False):
    """
    -> fatorial ele requeri dois valores,
    :param: num -> é o número que vai ser fatorado
    :param: show -> (opcional) é o parametro booleano que decide se vai aparecer a formula do fatorial ou não
    :return: O valor do resultado do fatorial   
    """
    f = 1
    for v in range(num, 0, -1):
        if show:
            print(v, end=' x ' if v > 1 else ' = ')
        f *= v
    print(f)


def show(valor):
    return valor.upper() == 'T'


s = show(input('T or F: '))
n = int(input('Digite um número pra fatorar: '))
fatorial(n, s)


#mais outra ficha de jogador só q com função agr

def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s)')

n = input('Insira o nome do jogador: ').strip()
g = input('Insira a quantidade de gols q o jogador marcou na partida: ').strip()

g = int(g) if g.isnumeric() else 0

if n == '':
    n = '<desconhecido>'

ficha(n, g)

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

def anal_nu():
    while True:
        valor = input('digite um valor: ')

        if valor.isdigit():
            print('parabens')
            return int(valor)
            break
        
        else:
            print('Erro!, valor invalido.')

n = anal_nu()
print(f'voce digitou {n}')

#NÃO CURSO
#notas, situações e dicionarios

def resumo(nome, idade=0, *notas):
    if len(nts) > 0:
        m = sum(nts) / len(nts)
        print(f'A média é {m:.2f}')
    else:
        print('a media é 0')
    print(nome, idade, m)


n = input('Manda teu nome: ')
i = int(input('Manda a idade: '))
nts = []
nts.append(float(input('Adicione a primeira nota: ')))
nts.append(float(input('Adicione a segunda nota: ')))
nts.append(float(input('Adicione a terceira nota: ')))

resumo(n, i, *nts)

#AGORA CURSO

print('___'*30)
def notas(*n, sit=False):
    """
    ->    LEIA    <-
    :param: *n, ele pega as notas que estão guardadas e as desempacota.
    :param: sit: (OPCIONAL) se você quiser exibir a "situação" vc deve usar sit=True.
    :return: dicionário com a nota, maior nota, menor nota, média e se vc quiser a situação entre:
    {RUIM, RAZOÁVEL E BOA}
    """
    if len(n) == 0:
        return {'ERRO!: NENHUMA NOTA INFORMADA!'}

    ficha = dict()
    ficha['total'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)
    m = sum(n) / len(n)
    ficha['media'] = f'{m:.2f}'

    if sit:
        if m < 5:
            ficha['situação'] = 'Ruim'

        elif m < 7:
            ficha['situação'] = 'Razoável'

        else:
            ficha['situação'] = 'bom'

    return ficha

n = (5.5, 9, 7)
resp = notas(*n, sit=True)
help(notas)


#CORZINHA PELA PRIMEIRA VEZ COMO REQUISITO YAY

def inter_help():
    print('\033[0;33;46m=-\033[0;37;40m'*13)
    print('\033[0;33;46m Interactive Help Python  \033[0;37;40m')
    print('\033[0;33;46m=-\033[0;37;40m'*13)
    ac = input('Função ou Biblioteca: ')
    print('\033[0;37;44m=-\033[0;30;40m'*13)
    print(f'\033[0;37;44m Acessando...           \033[0;37;40m')
    print('\033[0;37;44m=-\033[0;30;40m'*13)

    help(ac)

while True:
    wan = input('YES OR NO: [Y/N] ').upper()
    if wan == 'Y':
        inter_help()
    elif wan == 'N':
        adeus = input('TEM CERTEZA?!: [digite "FIM" se sim]: ').upper()
        if adeus == 'FIM':
            break
    else:
        print('ERROR! THE VALUE IS INCORRECT, TRY ONCE AGAIN!')

print(f'\033[0;31;47mADEUS!\033[0;30;40m')
'''