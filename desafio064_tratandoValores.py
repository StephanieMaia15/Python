#Soma de valores enquanto o numero digitado for diferente de 999
num = cont = soma = 0
num = int(input('Digite um número [999 para sair]'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para sair]: '))
print('Você digitou {} números e a soma entre eles foi:{} '.format(cont, soma))