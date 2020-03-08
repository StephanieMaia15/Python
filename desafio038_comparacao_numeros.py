#verificando se um numero é maior ou menor ou ainda se sao iguais.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O {} é maior que {} '.format(n2, n1))
else:
    print('Os valores sao iguais '.format())
