#calculando IMC
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é {:.1f} Você esta abaixo do peso'.format(imc))
elif imc == 18.5 or imc <= 25:
    print('Seu IMC é {:.1f} Seu peso é ideal.'. format(imc))
elif imc == 25.1 or imc <= 30:
    print('Seu IMC é {:.1f}: Sobrepeso.'.format(imc))
elif imc == 30.1 or imc <= 40:
    print('Seu IMC é {:.1f}: Obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f}: Obesidade mórbida.'.format(imc))

