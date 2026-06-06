'''#varificator os sexs ?

sexo = input('qual é o seu sexo?: [M/F] ').upper()[0].strip()
while sexo != 'M' and sexo != "F":
    if sexo not in ['M','F']:
        sexo = input('valor invalido, por favor, selecione apenas um dos dois: [M/F] ').upper()

print('legal')

#joguinho

import random
import time

tents = 0
num = random.randint(0,10)
print(f'{'-=-='*20}')
your_chance_to_be_a_BIG_SHOT = int(input('TENTE ADIVINHAR EM QUE \033[0;35mNÚMERO \033[0;37mESTOU PENSANDO!!! \033[0;30m(entre 0 e 10)\033[0;37m'))
print(f'{'-=-='*20}')

while your_chance_to_be_a_BIG_SHOT != num:
    if your_chance_to_be_a_BIG_SHOT > 10 or your_chance_to_be_a_BIG_SHOT < 0:
        your_chance_to_be_a_BIG_SHOT = int(input('... você por acaso sabe ler? '))
        print(f'{'____'*20}')
    elif your_chance_to_be_a_BIG_SHOT != num and tents < 4:
        your_chance_to_be_a_BIG_SHOT = int(input('VAMOS LÁ, \033[0;31mNEM ISSO VOCÊ CONSEGUE?!?!?! \033[0;30m(entre 0 e 10)\033[0;37m'))
        print(f'{'____'*20}')
    elif your_chance_to_be_a_BIG_SHOT != num and 8 > tents >= 4:
        your_chance_to_be_a_BIG_SHOT = int(input('\033[0;31mQUANTO TEMPO MAIS VAI LEVAR, HEIN? \033[0;30m(entre 0 e 10)\033[0;37m'))
        print(f'{'____'*20}')
    elif your_chance_to_be_a_BIG_SHOT != num and tents >= 8:
        your_chance_to_be_a_BIG_SHOT = int(input('\033[0;31mQUE PATÉTICO!!! \033[0;37m EU PENSEI QUE VOCÊ FOSSE MELHOR QUE \033[0;31mISSO!!! \033[0;30m (entre 0 e 10)\033[0;37m'))
        print(f'{'____'*20}')
    if your_chance_to_be_a_BIG_SHOT > -1 and your_chance_to_be_a_BIG_SHOT < 11:
        tents += 1
    else:
        tents += 0
time.sleep(2)
print('...')
time.sleep(2)
print('...')
time.sleep(2)
print('... parece... que...')
time.sleep(2)
print('...')
time.sleep(2)
print('...você...')
time.sleep(2)
print('...')
time.sleep(2)
print('...haha...')
time.sleep(2)
print('...')
time.sleep(2)
print('...')
time.sleep(2)
print('... quem diria... que...')
time.sleep(2)
print('...\033[0;31mvocê\033[0;37m...')
time.sleep(2)
print('...')
time.sleep(2)
print('...')
time.sleep(2)
print('...haha...')
time.sleep(2)
print('...')
time.sleep(2)
print('...\033[0;31mvo...')
time.sleep(1)
print('...cê...\033[0;37m')
time.sleep(5)
print(f'{'+=+='*20}')
if tents == 1:
    print(f'\033[0;33mVENCEU!!! \033[0;37mMEUS GRANDICISSÍMOS \033[0;36mPARABÉNS!!!\033[0;37m E LEVOU APENAS {tents} TENTATIVA!!!\n\033[0;30m(eu vou esquartejar você seu trapaceiro)\033[0;37m')
else:
    print(f'\033[0;33mVENCEU!!! \033[0;37mMEUS GRANDICISSÍMOS \033[0;36mPARABÉNS!!!\033[0;37m E LEVOU APENAS {tents} TENTATIVAS!!!')
print(f'DE FATO O NÚMERO QUE PENSEI ERA O \033[0;31m{num}\033[0;37m')
print(f'{'+=+='*20}')

#menu e valores

val1 = int(input('primeiro valor: '))
val2 = int(input('segundo valor: '))
escolha = 0

while escolha != 5:
    escolha = int(input(' [ 1 ] = + \n [ 2 ] = * \n [ 3 ] = maior \n [ 4 ] = novos valores \n [ 5 ] = sair \n escolha: '))
    if escolha == 1:
        r = val1 + val2
        print(f'{val1} + {val2} = r')
    elif escolha == 2:
        r = val1 * val2
        print(f'{val1} * {val2} = {r}')
    elif escolha == 3:
        r = val1 > val2
        if val1 > val2:
            print(f'{val1} > {val2}, {r}')
        else:
            print(f'{val1} > {val2}, {r}')
    elif escolha == 4:
        val1 = int(input('primeiro valor: '))
        val2 = int(input('segundo valor: '))
    else:
        print('algum valor foi digitado incorretamente, por favor, insira novamente o valor desejado')

#fatorial

comeco = int(input('De qual número o ser humano que está lendo isso deseja fatorar? '))
r = 1

while comeco > 1:
    print(comeco, end=' -> ')
    r *= comeco
    comeco -= 1

print(f'{comeco}\n{r}')

#melhoramento parte 1 do pa

p1 = int(input('selecione o primeiro termo: '))
r = int(input('selecione a razão: '))
decimo = p1 + 10 * r

while p1 < decimo:
    print(p1, '-> ', end='')
    p1 += r


print('cabo')

#melhoramento parte 2 do pa

ru = input('deseja proseguir: [S/N] ').upper()
ruq = 0
p1 = int(input('selecione o primeiro termo: '))
r = int(input('selecione a razão: '))
decimo = p1 + (10 - 1) * r

while ru == 'S':
    while p1 < decimo:
        print(p1, '-> ', end='')
        p1 += r
    ru = input('\ndeseja proseguir: [S/N] ').upper()
    if ru == 'S':
        ruq = int(input('quantas unidades a mais: '))
        decimo += ruq * r
    else:
        break

print('cabo')

#fibonacci

n = int(input('escolha um numero: '))
t1 = 0
t2 = 1
cont = 0

while cont < n:
    print(t1, end='-> ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
print('pronto')

# 999

num = save = qts = 0
while num != 999:
    print('--'*20)
    num = int(input('DIGITE NUMEROS (se quiser sair digite 999): '))
    if num != 999:
        save += num
        qts += 1
    else:
        break
print('--'*20)
print(f'foram digitados {qts} valore(s), e a soma resulta em {save} (tirando fora 999, já que ele não conta).')

#media, maior e menor com numero com demanda

ma = men = med = cont = tot = 0

print('_____'*20)
usu = input('Deseja proseguir?:[S/N] ').lower()

while usu != 'n':
    if usu == 's':
        print('_____'*20)
        num = int(input('digite qualquer número: '))
        if cont == 1:
            ma = num
            men = num
        else:
            if num > ma:
                ma = num
            elif num < men:
                men = num
        cont += 1
        tot += num
        if num > 0:
            med = tot / cont
        print('_____'*20)
        usu = input('Deseja proseguir?:[S/N] ').lower()
    else:
        print('_____'*20)
        usu = input('Acho que houve algum erro de digitação, por favor digite corretamente:[S/N] ').lower()

print('_____'*20)
print(f'A média de todos os números é {med}, o maior foi {ma} e o menor foi {men}')

#tabuada melhorada

n = int(input('manda numeroxx pra tabuada: '))
tab = 1

while True:
    if n > 0:
        r = n * tab
        print(f'{tab} X {n} = {r}')
        tab += 1
        if tab > 10:
            print('-=' * 20)
            n = int(input('manda numeroxx pra tabuada: '))
            tab = 1
            print('-=' * 20)
    else:
        break
print('programa encerrado.')
#

import random
import time

time.sleep(1)
print('...')
time.sleep(1)
print('+=-=' * 20)
print('SEJA MUITO MUITO BEM-VINDO!!!')
print('+=-=' * 20)
time.sleep(1)

rod = 0
peninha = 'jogador venceu, mais uma rodada!'
haha = 'MAS QUE PENINHA, MAIS SORTE NA PRÓXIMA!'

while True:
    compj = random.randint(1,10)
    joge = input('PAR OU ÍMPAR ').strip().upper()
    print('_____'*20)
    jogj = int(input('M-M-MANDE SEU LANCE!!! [qualquer número entre 1 e 10]: '))
    print('_____'*20)
    if (jogj + compj) % 2 == 0:
        par = True
        if par == True:
            if joge == 'PAR':
                print(peninha)
                print(f'jogada do jogador {jogj} / jogada do computador {compj}')
                print(f'resultado é {jogj + compj}, deu PAR!')
                print('_____'*20)
                rod += 1
            else:
                print(haha)
                print('_____'*20)
                break
    else:
        par = False
        if par == False:
            if joge == 'IMPAR':
                print(peninha)
                print(f'jogada do jogador {jogj} / jogada do computador {compj}')
                print(f'resultado é {jogj + compj}, deu PAR!')
                print('_____'*20)
                rod += 1
            else:
                print(haha)
                print('_____'*20)
                break
print(f'o jogador venceu {rod} partida(s)!!!')
print(f'jogada do jogador {jogj} / jogada do computador {compj}')
print(f'but, apostou no {joge}')

#cadastro

print('===========CADASTRO==============')

idade = maior18 = men = womanlessthan20 = 0
sexo = ''
forward = input('Deseja inserir dados?: [S/N] ').upper().strip()

while True:
    if forward == 'S':
        idade = int(input('informe sua idade: '))
        sexo = input('informe seu sexo: [M/F] ').upper().strip()
        if sexo != 'M' and sexo != 'F':
            sexo = input('houve um erro de digitação, informe seu sexo corretamente: [M/F] ').upper().strip()
        print('--'*20)
        forward = input('Deseja inserir mais dados?: [S/N] ').upper().strip()
        if forward != 'S' and forward != 'N':
            forward = input('Houve um erro de digitação, ainda quer inserir mais dados?: [S/N] ').upper().strip()
        if idade >= 18:
            maior18 += 1
        if sexo == 'M':
            men += 1
        else:
            if idade < 20:
                womanlessthan20 += 1
    elif forward == 'N':
        break
    else:
        forward = input('AINDA QUER FICAR OU NÃO?: [S/N] ').upper().strip()

print('--'*20)
print(f'O total de pessoas que se castraram com 18 anos ou mais são de {maior18}')
print(f'O total de homens que se castraram são de {men}')
print(f'O total de mulheres que se castraram com mais de 20 anos são de {womanmoreless20}')

#quase um mercado

prec = tot = mais1000 = baratinho = 0
nome_prodt = nome_baratinho = ''
cont = input('deseja prosseguir?: [S/N] ').upper().strip()

while True:
    if cont == 'S':
        print('___' * 20)
        nome_prodt = input('Qual o nome do produto?: ')
        prec = float(input('qual o valor do produto?: '))
        cont = input('deseja prosseguir?: [S/N] ').upper().strip()
        tot += prec
        if tot == prec:
            baratinho = prec
            nome_baratinho = nome_prodt 
            c += 1
        else:
            if prec < baratinho:
                baratinho = prec
                nome_baratinho = nome_prodt  
        if prec > 1000:
                mais1000 += 1
    elif cont == 'N':
        break
    else:
        cont = input('digitação incorreta, deseja prosseguir?: [S/N] ').upper().strip()
print(f'{tot:.2f}')
print(f'{mais1000} e {nome_baratinho}')
#

nota = 50
totced = 0
dindin = int(input('Quanto vc saca?: '))
total = dindin

while True:
    if total >= nota:
        total -= nota
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totced = 0

        if total == 0:
            break
#'''

