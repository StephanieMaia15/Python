#calculando o valor a pagar de multa de acordo com a quilometragem excedida
v = float(input('Quantos KM/H esta o carro? '))
km = v - 80
multa = 7 * km
exc = km % v
if v > 80:
    print('Seu carro ultrapassou em {:.0f} KM a velocidade máxima permitida. A multa é de 7 reais para cada quilometro acima do limite. A multa é de: R${} '.format(exc, multa))
else:
    print('Dentro da velocidade permitida para essa estrada')

