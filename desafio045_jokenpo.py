#jogando Jokenpô com o computador
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções: 
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Escolha uma opção: ?'))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA \nJogue novamente')

else:
    print('Eu escolhi {}'.format(itens[computador]))
    print('Você escolheu {}'.format(itens[jogador]))
print('#-#' * 11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você venceu')
    elif jogador == 2:
        print('Eu ganhei')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Eu ganhei')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Você venceu')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Você venceu')
    elif jogador == 1:
        print('Eu ganhei')
    elif jogador == 2:
        print('Empate')




