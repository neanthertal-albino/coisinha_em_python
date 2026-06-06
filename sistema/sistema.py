from interface import configsistem
from time import sleep
from arquivos import *

arq = 'coisinha_em_python/sistema/curso.txt'

if not arqexiste(arq):
    criararquivo(arq)
    print('Arquivo criado com sucesso!')

while True:
    resposta = configsistem.menu(['Cadastrar', 'Lista dos cadastrados', 'Sair do sistema'])
    if resposta == 1:
        #cadastro
        configsistem.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = configsistem.leia_int('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 2:
        #Opção de listar o conteúdo de um arquivo!
        lerarquivo(arq)

    elif resposta == 3:
        configsistem.cabecalho('Saindo do sistema... até logo!')
        break

    else:
        print('\033[31mERRO!\033[m Digite uma opção válida.')
    sleep(1)