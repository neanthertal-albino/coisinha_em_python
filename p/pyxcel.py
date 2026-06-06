nomes = ['Ana', 'Lucas', 'Maria']
idades = ['19', '22', '18']

with open('coisinha_em_python/p/teste.csv', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Nome;Idade\n')
    
    for i in range(len(nomes)):
        linha = f'{nomes[i]};{idades[i]}\n'
        arquivo.write(linha)
