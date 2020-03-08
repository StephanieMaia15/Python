#Tentando adivinhar o número que o computador escolheu entre 1 e 5
from random import randint
from time import sleep
lista = randint(0, 5)
numero = lista
n = int(input('Qual número você acha que foi sorteado? '))
print('Processando...')
sleep(2)
if n > 5:
    print('Este número não esta dentro do sorteio')
print('Parabens, você esta correto!' if numero == n else 'Tente novamente!')
print('O número sorteado foi: {}'.format(numero))