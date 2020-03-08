#Condições
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6.0:
    print('Sua média foi: {:.1f} Parabéns!'.format(m))
else:
    print('Sua média foi: {:.1f} Nota abaixo do esperado.'.format(m))
