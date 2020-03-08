#Entendo uma condiçao aninhada

nome = str(input('Digite seu nome: '))
if nome == 'Stephanie':
    print('{}, seu nome é lindo!'.format(nome))
elif nome == 'Joana' or nome == 'Maria' or nome == 'Pedro' or nome == 'João':
    print('Seu nome é bem comum. ')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Esse nome esta na lista de nomes femininos no Brasil')
else:
    print('{}, seu nome é bem diferente'.format(nome))
print('Tenha um ótimo dia! ')