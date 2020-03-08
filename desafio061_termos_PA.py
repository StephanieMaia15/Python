#calculando o primeiro termo e razao de uma P.A com while

print('Gerador de PA')
print(' - ' * 10) # linha de separacao opcional
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
