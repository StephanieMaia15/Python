#encontrando a quantidade de letras antes do primeiro espaço
nome = str(input('Digite o seu nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print('Seu primeiro nome tem {} letras :'.format(nome.find(' ')))






