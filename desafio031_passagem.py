#calculando o valor da passagem de acordo com a KM percorrida.
#distancia = float(input('Quantos KM de distancia tem sua viagem?'))
#km = 0.50
#km2 = 0.45
#total1 = distancia * km
#total2= distancia * km2
#if distancia <= 200:
 #   print('O valor total da sua viagem é: R$ {:.2f} '.format(total1))
#else:
    #print('O valor total da sua viagem é R$ {:.2f} '. format(total2))

    #IF e ELSE simplificado:
distancia = float(input('Digite a distancia da viagem: '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da viagem é: R${:.2f}'.format(preco))