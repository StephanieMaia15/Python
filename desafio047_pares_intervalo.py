#verificando quais numeros sao pares em uma lista de 50 numeros
for c in range(1, 51):
    par = c % 2
    if par == 0:
        print('\33[0:44m{} É PAR\33[m'.format(c))
    else:
        print('\33[0:46m{} É IMPAR!!\33[m'.format(c))



