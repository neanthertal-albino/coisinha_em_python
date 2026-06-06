'''#tuplas

ne = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
nu = int(input('digite um número entre 0 e 20: '))

while nu < 0 or nu > 20:
    nu = int(input('por favor, digite um número ENTRE 0 e 20: '))
    if nu >= 0 and nu < 21:
            break

print(f'voce digitou o numero {ne[nu]}')
#

#BRASILEIRÃO

times = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Bahia', 'athletico-PR', 'Coritiba', 'Bragantino', 'BotaFogo', 'Vasco da Gama', 'EC Vitória', 'Grêmio', 'Internacional', 'Santos', 'Cruzeiros', 'Mirassol', 'Remo', 'Chapecoense')

print(f'Os 5 primeiros times são: {times[0:5]}')
print('--'*20)
print(f'Os 4 ultimos times são: {times[14:20]}')
print('--'*20)
print(f'na ordem alfabética: {sorted(times)}')
print('--'*20)
print(times.index('Chapecoense'))


#sorteio

from random import randint

n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(n)
print(f'o maior foi {max(n)} e o menor foi {min(n)}')

#analise de dados

n = (   int(input('Insira o primeiro valor: ')),
        int(input('Insira o segundo valor: ')),
        int(input('Insira o terceiro valor: ')),
        int(input('Insira o quarto valor: ')))
print('--'*20)
v9 = c = 0

while True:
    if n[c] == 9:
        v9 += 1
    c += 1
    if c >= 4:
        break

c = 0
p = -1

while c < len(n):
    if n[c] == 3:
        p = c
        break
    else:
        c += 1

pa = []

for par in range(len(n)):
    if n[par] % 2 == 0:
        pa.append(n[par])

print(f'Voce digitou os valores {n}')
if p != -1:
    print(f'O 3 foi achado na posição {p}')
else:
    print('o caba nao foi achado...')
if v9 > 0:
    print(f'temos {v9} noves aqui')
else:
    print('o nove nao foi digitado nenhuma vez')
print(f'esse foram todos os pares digitados {pa}')

#Lista
lista = ('Pão', 6.99, 'Caixa de Leite 1lt', 12.539, 'queijo', 5.99, 'yogurt', 12.99, 'lápis', 2.99)

print('==' * 20)
print(f'LISTAGEM DE PRODUTOS'.center(40))
print('==' * 20)

for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30} R$ {lista[i + 1]:>5.2f}')

#

#verificador de vogais

f = ('TRABALHAR', 'VERBO', 'SEILA', 'MICHAL JACKSON', 'AIR FRIER', 'URSO', 'MACACO', 'GRAMA')

for palavra in f:
    print(f'\nPara cada {palavra} temos ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra}', end=' ')

#FIM TUPLAS

#testando

v = []
v.append(2)
v.append(9)
v.append(7)

for c, v in enumerate(v):
    print(f'achei o valor {v} na posição {c}')


#seila indice e valores

v = [int(input('INSIRA O PRIMEIRO VALOR: ')), int(input('INSIRA O SEGUNDO VALOR: ')), int(input('INSIRA O TERCEIRO VALOR: ')), int(input('INSIRA O QUARTO VALOR: ')), int(input('INSIRA O QUINTO VALOR: '))]
vm = vl = v[0]
valormaiorindice = []
valormenorindice = []

for i, valor in enumerate(v):
    if valor > vm:
        vm = valor
    elif valor == vm:
        valormaiorindice.append(i)

    if valor < vl:
        vl = valor
    elif valor == vl:
        valormenorindice.append(i)

print(f'O MAIOR valor foi {vm} que esta na posição {valormaiorindice}\nO MENOR valor foi {vl} que está na posição {valormenorindice}')

#valores usando sort
v = 0
l = []

while True:
    p = str(input('DESEJA CONTINUAR: [SIM/NAO] ')).upper()
    if p == 'SIM':
        v = int(input('DIGITE ALGUM VALOR: '))
        if v in l:
            print('DIGITE UM VALOR DIFERENTE!')
        else:
            l.append(v)
    elif p == 'NAO':
        break
    else:
        p = input('DIGITOU ERRADO, DESEJA CONTINUAR: [SIM/NAO] ').upper()

l.sort()
print(l)
#
num = []

for i in range(0,5):
    ve = int(input('DIGITE ALGUM VALOR: '))
    if num == [] or ve > num[-1]:
        num.append(ve)
    else:
        pos = 0
        while pos < len(num):
            if ve <= num[pos]:
                num.insert(pos, ve)
                break
            pos += 1
print(f'Os valores da lista em ordem são {num}')

#valores listas poggers

valores = []

while True:
    quer = input('quer: [s/n] ').lower().strip()
    if quer == 's':
        val = int(input('digita seu numero: '))
        valores.append(val)
    elif quer == 'n':
        print('aff')
        break
    else:
        print('nigger')

print(len(valores))
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('5 foi digitado, parabens')
else:
    print('5 nao foi digitado, unhe')

#num lista par e impar

num = []
par = []
impar = []


while True:
    quer = input('SIM OU NAO: ').upper().strip()
    if quer == 'SIM':
        v = int(input('DIGITE UM VALOR: '))
        num.append(v)
    elif quer == 'NAO':
        print('ta')
        break

for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'isso foi tudo {num}\nisso foi os pares {par}\ne isso foi os impares {impar}')

#guanabara desafio

expressao = input('digite sua expressão: ')
pilhatoeatshit = []

for i in expressao:
    if i == '(':
        pilhatoeatshit.append('(')
    
    elif i == ')':
        if len(pilhatoeatshit) > 0:
            pilhatoeatshit.pop()
        else:
            pilhatoeatshit.append(')')
            break
    
if len(pilhatoeatshit) == 0:
    print('expressão poggers')
else:
    print('You should eat shit')
#

#avaliando pessoas e pesos

pessoas = []
pmap = []
pmep = []
dados = []
keep = ''

while True:
    keep = str(input('Quer prosseguir?: [s/n]')).lower().strip()
    if keep == 's':
        dados.append(input('Insira seu Nome: '))
        dados.append(int(input(f'Insira seu peso: ')))
        print('-='*20)
        pessoas.append(dados[:])
        dados.clear()

    elif keep == 'n':
        break

    else:
        print('Ops, algum valor foi digitado incorretamente')
        print('____'*20)


ma = me = pessoas[0][1]

for i in range(len(pessoas)):
    if pessoas[i][1] > ma:
        ma = pessoas[i][1]

    elif pessoas[i][1] < me:
        me = pessoas[i][1]

for pessoa in pessoas:
    if pessoa[1] == ma:
        pmap.append(pessoa[0])
    
    elif pessoa[1] == me:
        pmep.append(pessoa[0])


print('____'*20)
print(f'O total {len(pessoas)} de pessoas cadastradas aqui')
print(f'O maior peso foi de {ma} de {pmap}')
print(f'O mais leve foi de {me} de {pmep}')

# mais uma lista de numeros pares e impares

num = []
par = []
impar = []

for v in range(0,7):
    valor = int(input('Insira algum valor: '))
    num.append(valor)

for i, v in enumerate(num):
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        impar.append(num[i])

impar.sort()
par.sort()

print(impar)
print(par)


#matriz 

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'insira o valor para a posição [{l}, {c}] '))

print('-='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()



#matriz e dados

par = []
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = soma = soma3 = maior2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'INSIRA O VALOR PARA [{l} {c}]: '))

        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
        
for c in range(len(matriz)):
    if matriz[1][c]:
        if maior2 == 0 or matriz[1][c] > maior2:
            maior2 = matriz[1][c]

print('+='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for v in range(len(par)):
    soma = soma + par[v]

for l in range(len(matriz)):
    if matriz[l][2]:
        soma3 = soma3 + matriz[l][2]


print('-='*30)
print(soma)
print(soma3)
print(maior2)

#não aguento mais
#MEGA SENA

import random

jogos = []
numeros = []
quantidade = int(input('Quantos jogos vc quer?: '))

for q in range(quantidade):
    
    numeros = sorted(random.sample(range(1, 61), 6))
    numeros.sort()
    
    if len(numeros) == 6:
        jogos.append(numeros[:])
        numeros.clear()
    
for i, j in enumerate(jogos):
    print(f'O jogo N{i+1} é {j}')


#media, nota, aluno... denovo...

alunos = []
notas = []
nome = ''
nota = nota2 = media = 0

while True:
    inserir = input('Deseja inserir mais notas?: [S/N] ').upper().strip()
    print('___' * 20)

    if inserir == 'S':
        nome = input('Qual é o nome do aluno?: ')
        nota = float(input('A primeira nota desse aluno: '))
        notas.append(nota)
        nota2 = float(input('A segunda nota desse aluno: '))
        print('___' * 20)
        media = (nota + nota2) / 2
        notas.append(nota2)
        alunos.append([nome, [nota, nota2], media])
        notas.clear()
    
    elif inserir == 'N':
        print('___' * 20)
        break

    else:
        print('Valor incorreto...')

print(f'{'Id':<4}', f'{'nome':<10}', f'{'media':>10}')
for i, v in enumerate(alunos):
    print(f'{i:<4} {v[0]:<10} {v[2]:>10}')

while True:
    opc = int(input('mostrar notas de qual aluno?: [999 interrompe] '))
    if opc == 999:
        break
    if opc <= len(alunos) - 1:
        print(f'Notas do aluno {alunos[opc][0]} são {alunos[opc][1]}')
        print('___'*30)
'''