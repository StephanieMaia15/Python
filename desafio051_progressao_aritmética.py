#Contando de um numero a outro de acordo com o valor solicitado
primeiro = int(input('Digite o primeiro termo: ')) #numero para comecar a contar
razao = int(input('Qual a razão? ')) #contando de quanto em quanto
decimo = primeiro + (10 - 1) * razao #formula matematica para leitura
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='> ')
print('Acabou!')


