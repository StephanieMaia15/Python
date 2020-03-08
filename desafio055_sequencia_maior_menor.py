#Lendo o peso de uma pessoa e mostrando qual o menor e o maior peso da lista
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}˚ pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))


