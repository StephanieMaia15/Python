#verificando se um numero é par ou impar
n = int(input('Digite um numero: '))
par = n % 2
if par == 0:
    print('O número {} é par'.format(n))
else:
    print(' {} é ímpar '.format(n))

