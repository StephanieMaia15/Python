#verificando quais numeros sao impares em uma lista de um ate 500 e realizando a soma deles
soma = 0
cont = 0
for c in range(1, 501, 2):# 2 = pulando de dois em dois
   if c % 3 == 0:
       soma += c
       cont += 1
print('\33[0:44mA soma dos {} valores multiplos por 3 é: {}\33[m'.format(cont, soma))

