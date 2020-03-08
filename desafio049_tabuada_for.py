#Mostrando a tabuada de um número de acordo com a solicitacao do usuario
num = int(input('Digite a tabuada que voce quer: '))
for c in range(1, 11):
    print('{} x {:2} = {} '.format(num, c, num*c))
