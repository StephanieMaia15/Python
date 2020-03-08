#calculando o fatorial de um numero com módulo

from math import factorial
n = int(input('Digite um número para calcular o fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# calculando o fatorial de um numero com While
n = int(input('Digite um número para calcular o fatorial:'))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
