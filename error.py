'''#tratando erro
def leia_int(msg):
    while True:
        try:
            print('___'*20)
            n = int(input(msg))
            
        except (ValueError, TypeError):
            print('___'*20)
            print('\033[31mERRO: Algum valor foi digitado incorretamente, por favor.\033[m')
            continue
        
        except KeyboardInterrupt:
            print('___'*20)
            print('\033[31mO usuário preferiu não informar nenhum valor.\033[m')
            break

        else:
            return n


def leia_float(msg):
    while True:
        try:
            print('___'*20)
            n = float(input(msg))
            
        except (ValueError, TypeError):
            print('___'*20)
            print('\033[31mERRO: Algum valor foi digitado incorretamente, por favor.\033[m')
            continue
        
        except KeyboardInterrupt:
            print('___'*20)
            print('\033[31mO usuário preferiu não informar nenhum valor.\033[m')
            break

        else:
            return n


num = leia_int('Digite um valor INTEIRO: ')
num2 = leia_float('digite um valor REAL:')

if num != None and num2 != None:
    print(f'O valor inteiro foi {num} e o valor real foi {num2}')

elif num == None and num2 != None:
    print(f'O único valor inserido foi o REAL {num2}')

elif num != None and num2 == None:
    print(f'O único valor inserido foi o INTEIRO {num}')

else:
    print('Nenhum valor inserido.')

#SITE PUDIM KAKAKKAKAKAKAKA
 
import requests

url = "https://pudim.com.br"

try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print("Site do Pudim está acessível")
        
    else:
        print(f"Site respondeu, mas com erro: {resposta.status_code}")
except requests.exceptions.RequestException:
    print("Site do pudim infelizmente não está acessível")
    
#'''

