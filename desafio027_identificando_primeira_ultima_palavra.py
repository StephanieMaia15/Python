n = str(input('Digite nome e sobrenome: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {} '.format(nome[len(nome)-1]))  #removendo a posiçao 0)

