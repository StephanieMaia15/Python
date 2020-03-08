while True:
    num = int(input('Digite um valor para ver a tabuada: '))
    if num == -1:
        print('Valor incorreto! Obrigada pela visita! ')
        break
    for c in range(1, 11):
        print('{} x {:2} = {} '.format(num, c, num * c))



