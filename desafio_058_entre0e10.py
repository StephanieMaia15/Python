##jogo: tentar adivinhar o numero ate acertar
from random import randint
numsorteado = randint(1, 10)
print('Tente adivinhar um número sorteado de 1 à 10...')
jogada = int(input('Qual o seu palpite: '))
cont = 1
while jogada != numsorteado:
    if jogada > numsorteado:
        print('Informe outro valor')
    jogada = int(input('Tente novamente: '))
    cont += 1
print('Parabéns, com {} tentativas você venceu! Eu escolhi o número {}!!!' .format(cont, numsorteado))