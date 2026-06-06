'''nome = str(input('olá, qual é seu nome?: '))
if nome == 'BANANA VOADORA':
    print('seloko nome zika kakakakakakakaka')
elif nome == 'sigma' or nome == 'Optimus Prime' or nome == 'calango':
    print('vc é muito chad based')
elif nome == 'EU NAO TENHO NOME':
    print('buxa')
else:
    print(f'nao podexx, somente o {nome}')
print('bom dia {}'.format(nome))

#vereficador de emprestimos

valor_house = float(input('Ae maluco, qual o valor da casa?: '))
sal = float(input('quanto q cê recebe?: '))
anos = int(input('quanto tempo pretende pagar?: '))
empre = valor_house / (anos * 12)
mini = sal * 30 / 100
print(f'prestação será de {empre:.2f}, pois vc quer uma casa de {valor_house}, com um salario de {sal} num intervalo de {anos}')

if empre <= mini:
    print('emprestimo pode ser CONCEDIDO')
else:
    print('emprestimo NEGADO')


#convertedor de numero

num = int(input('Escolha um número inteiro qualquer: '))
choice = int(input('---------------------------------------- \n Insira sua base de conversão: \n 1-Binário \n 2-octal \n 3-hexadecimal \n '))
if choice == 1:
    print(bin(num)[2:])
elif choice == 2:
    print(oct(num)[2:])
elif choice == 3:
    print(hex(num)[2:])
else:
    print('paia')


#  verificador de numero

num1 = int(input('Insira um número: '))
num2 = int(input('Por favor, insira um número novamente: '))

if num1 > num2:
    print(f'o primeiro número {num1} é maior que o segundo {num2}')
elif num1 < num2:
    print(f'o primeiro número {num1} é menor que o segundo {num2}')
else:
    print(f'os dois numeros são iguais ({num1})')


#sistema verificador de idade para alistamento militar
print('{===================================\n ALISTAMENTO MILITAR \n}')
from datetime import date
atual = date.today().year
nac = int(input('informe o ano de seu nascimento: '))
ida = atual - nac

if ida == 18:
    print('\n--------------------------\nEstá na hora de se alistar, você tem {} anos\n--------------------------'.format(ida))
elif ida < 18:
    espe = 18 - ida
    if espe == 1:
        anos = "ano"
    else:
        anos = "anos"
    prazo = atual + espe
    print(f'--------------------------\nMuito cedo, vc tem {ida} anos de idade, ainda falta {espe} {anos}\n--------------------------')
    print(f'------------------------------\nSeu alistamento deverá ser em {prazo} \n------------------------------')
elif ida > 18:
    dem = ida - 18
    if dem == 1:
        anos = "ano"
    else:
        anos = "anos"
        prazo = atual - dem
    print(f'\n--------------------------\ntarde demais, vc tem {ida} anos, já deveria ter se alistado a {dem} {anos} atras\n--------------------------')
    print(f'--------------------------\n vc deveria ter se alistado em {prazo} \n--------------------------')

#nota de aluno

nota1 = float(input('insira a primeira nota do aluno: '))
nota2 = float(input('insira a segunda nota do aluno: '))

media = (nota1 + nota2) / 2
print(media)
if media >= 7:
    print('Aprovado')
elif media < 5:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperação')


#nadador

idade = int(input('quão velho vc é: '))

if idade <= 9:
    print('nadador MIRIM')
elif idade <= 14:
    print('Nadador INFANTIL')
elif idade <= 19:
    print('nadador JUNIOR')
elif idade <= 25:
    print('nadador SENIOR')
elif idade > 25:
    print('nadador MASTER')


#triangulos v2

lad1 = int(input('Insira um valor: '))
lad2 = int(input('Insira um segundo valor: '))
lad3 = int(input('Insira um terceiro valor: '))

if lad1 + lad2 >= lad3 and lad3 + lad1 >= lad2 and lad2 + lad3 >= lad1:
    print('triangulo')
    if lad1 == lad2 and lad2 == lad3:
        print('triangulo equilatero')
    elif lad1 == lad2 != lad3 or lad2 == lad3 != lad1 or lad3 == lad1 != lad2:
        print('triangulo isoceles')
    elif lad1 != lad2 != lad3 != lad1:
        print('triangulo escaleno')
    else:
        print('seila oq tu criou ae KAKAKAKAKAKAKAKAKAKA')
else:
    print('not triangulo')

#imc

peso = float(input('quanto vc pesa: '))
altura = float(input('quanto vc mede: '))

imc = peso / (altura**2)
print(f'seu imc é {imc:.2f}')
if imc < 18.5:
    print('muito abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('vc esta no peso ideal')
elif imc > 25 and imc < 30:
    print('vc está sobrepeso')
elif imc > 30 and imc < 40:
    print('vc está obeso')
elif 40 < imc < 50:
    print('vc ta obeso mórbido')
else:
    print('cara, como vc ta vivo?')


#descontos e juros

prod = float(input('insira o preço da compra: '))
cond = int(input('Qual será a forma de pagamento\n  1-cheque/dinheiro\n  2-a vista cartão\n  3-até 2x no cartão\n  4-3x ou mais no cartão\n'))
if cond == 1:
    desc = prod * 10 / 100
    newpro = prod - desc
    print(f'valor novo a pagar com desconto {newpro}')
elif cond == 2:
    desc = prod * 5 / 100
    newpro = prod - desc
    print(f'o valor do produto a ser pago será {newpro}')
elif cond == 3:
    print('sem desconto, paga {}'.format(prod))
elif cond == 4:
    juro = prod * 20 / 100
    newprod = prod + juro
    parc = int(input('quantas parcelas?: ' ))
    tot = newprod / parc
    print(f'parcelas total {parc} valendo {tot:.2f}')
    print(f'valor do produto antes {prod} agr ficou {newprod}')
else:
    print('o doença, nao sabe ler nao?')


# pedra, papel e tesoura

import random
import time

play1 = input('jogador 1, Escolha entre pedra, papel e tesoura: ').upper()
play2 = random.randint(1,3)

if play2 == 1:
    play2 = 'PEDRA'
elif play2 == 2:
    play2 == 'PAPEL'
else:
    play2 = 'TESOURA'

print('PREPARADOS!')
time.sleep(1)
print('JÓ...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PÔ!')

if play1 == 'PEDRA' and play2 == 'PEDRA':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('EMPATE!')
elif play1 == 'PEDRA' and play2 == 'PAPEL':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('Jogador 2 venceu')
elif play1 == 'PEDRA' and play2 == 'TESOURA':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('Jogador 1 venceu')
elif play1 == 'PAPEL' and play2 == 'PEDRA':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('Jogador 1 venceu')
elif play1 == 'PAPEL' and play2 == 'PAPEL':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('EMPATE!')
elif play1 == 'PAPEL' and play2 == 'TESOURA':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('Jogador 2 venceu')
elif play1 == 'TESOURA' and play2 == 'PEDRA':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('jogador 2 venceu')
elif play1 == 'TESOURA' and play2 == 'PAPEL':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('jogador 1 venceu')
elif play1 == 'TESOURA' and play2 == 'TESOURA':
    print(f'jogador 1 jogou {play1} e jogador 2 jogou {play2}')
    print('EMPATE!')
#'''
