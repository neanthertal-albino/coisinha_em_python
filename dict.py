'''#alunol, media e dicionario
nome = str(input('Qual o nome do aluno?: '))
media = float(input(f'Qual é a média de {nome}?: '))

if media < 7:
    sita = 'REPROVADO'
else:
    sita = 'APROVADO'
    

ficha = {
    'nome': nome,
    'media': media,
    'situacao': sita
}

print(f'O nome do aluno(a) é {ficha["nome"]}.')
print(f'a média do(a) {ficha["nome"]} é {ficha["media"]}')
print(f'O aluno está {ficha["situacao"]}')

#dados jogadores

import random
from operator import itemgetter


jog = {
    'jogador1': random.randint(1,6),
    'jogador2': random.randint(1,6),
    'jogador3': random.randint(1,6),
    'jogador4': random.randint(1,6)
}
rank = list()

for i, v in jog.items():
    print(f'{i} tirou {v}')

rank = sorted(jog.items(), key=itemgetter(1), reverse=True)
print('_'*60)

for i, v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')


#DADOS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA 
from datetime import datetime

dados = dict()
dados['nome'] = input('Qual é teu nome?: ')
nasc = int(input(f'Em que ano {dados["nome"]} nasceu?: '))
dados['idade'] =  datetime.now().year - nasc
dados['ctps'] = int(input('MANDE A CARTEIRA DE TRABALHO: [0 nao tem] '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['sal'] = int(input('Salario: '))
    dados['aposen'] = dados['idade'] + (dados['contratação'] + 35 - datetime.now().year)

for v, k in dados.items():
    print(f'- {v} tem o valor {k}')
#JOGADOR BOLA

jogador = dict()

gol = []
jogador['nome'] = input('Qual o nome do jogador?: ')
jogador['part'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))

for p in range(jogador['part']):
    gol.append(int(input(f'Quantos gols o {jogador["nome"]} fez na {p+1} partida?: ')))

jogador['gol'] = gol[:]
totgol = sum(gol)

print(f'o jogador {jogador["nome"]} fez {totgol} gol(s) durante {jogador["part"]} jogos')

#media, pessoasa e cadastro completo

pessoa = dict()
muie = list()
pessoamaisvelhaqmedia = list()
ficha = list()

while True:
    pessoa.clear()
    print('_____'*20)
    prog = input('Quer continuar?: [S/N] ').upper().strip()

    if prog == 'S':
        pessoa['nome'] = input('NOME: ')
        pessoa['idade'] = int(input('IDADE: '))
        pessoa['sexo'] = input('QUAL TEU SEXO? [M/F] ').upper()

        while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            pessoa['sexo'] = input('INSIRA APENAS OS VALORES AO LADO [M/F] ').upper()
        ficha.append(pessoa.copy())
        
    elif prog == 'N':
        break

    else:
        print('DIGITADO ERRADO, APENAS DIGITE [S/N]')

total = totp = media = 0

print('=-'*30)
for p in ficha:
    total += p['idade']
    totp += 1
    media = total / len(ficha)

    if p['sexo'] == 'F':
        muie.append(ficha[:])
    
    if p['idade'] > media:
        pessoamaisvelhaqmedia.append(ficha[:])

print(f'- O total de pessoas é {totp}')
print(f'- A media é da idade de pessoas é {media:.2f} anos')
if len(muie) == 0:
    print(f'- nenhuma muie')
elif len(muie) == 1:
    print('- tem uma mulher cadastrada')
elif len(muie) > 1:
    print(f'- tem {len(muie)} mulheres cadastradas')
if len(pessoamaisvelhaqmedia) == 0:
    print('- niguem tem a idade maior que media')
else:
    print(f'- Tem {len(pessoamaisvelhaqmedia)} pessoas com a idade maior que a media, são o(s)\n{pessoamaisvelhaqmedia}')
#'''

#JOGADOR BOLA V2

time = list()
jogador = dict()
gol = []

while True:
    envi = input('CONTINUARXXX OU NÃO CONTINUARXXX: [S/N] ').strip().upper()
    if envi == 'S':
        print('__'*30)
        jogador['nome'] = input('Qual o nome do jogador?: ')
        jogador['part'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))

        gol = []

        for p in range(jogador['part']):
            gol.append(int(input(f'Quantos gols o {jogador["nome"]} fez na {p+1} partida?: ')))

        jogador['gol'] = gol[:]
        jogador['totgol'] = sum(gol)
        str(jogador['gol'])

        time.append(jogador.copy())

    elif envi == 'N':
        break

    else:
        print('mano, vc digitou algo errado neguinho.')
    print('___'*30)

print('___'*30)
print(f'{"Cod":<5}', f'{"Nome":<15} {"Gols":^20}', f'{"total":>30}')
for i, j in enumerate(time):
    print(f'{i:<5} {time[i]["nome"]:<23} {str(time[i]['gol']):<15} {time[i]['totgol']:^50}')
print('___'*30)

while True:
    mostrar = int(input('Qual jogador deseja mostrar? [999 interrompe o programa]: '))
    print('____'*30)
    if mostrar == 999:
        break
    
    elif mostrar > len(time):
        print(f'Não exixte jogador {mostrar}')

    elif mostrar != 999:
        print(f'=LEVANTAMENTO DO JOGADOR {time[mostrar]['nome']}=')
        for j in range(time[mostrar]['part']):
            if time[mostrar]['gol'][j] == 0:
                print(f'- na partida {j} não fez nenhum gol')
            
            elif time[mostrar]['gol'][j] == 1:
                print(f'- na partida {j} fez 1 gol')
            
            else:
                print(f'- na partida {j} fez {time[mostrar]['gol'][j]} gols')
        print('____'*30)
    
    