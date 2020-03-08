from random import randint
print('-'*30)
print('Jogo do Par ou Ímpar')
print('-'*30)
tot = ''
cont = 0
while True:
    n = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).upper().strip()
    pc = randint(0, 100)
    s = n + pc
    cont += 1
    if s % 2 == 0:
        tot = 'Par'
    else:
        tot = 'Impar'
    print(f'Você escolheu {n} e o computador {pc}. A soma deu: {s}. Esse número é:{tot}')
    if s == 'Par' and escolha == 'p':
        print('Você venceu!!')
    else:
        print('Eu ganhei!!')
        break
print(f'Você precisou realizar {cont} jogadas')