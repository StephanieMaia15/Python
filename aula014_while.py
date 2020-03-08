#usando o while
n = 1
par = impar = 0
while n != 0: #enquanto o valor digitado for diferente de zero, o programa continuara pedindo um valor
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0: # restante da divisao for igual a zero
             par += 1 # += pode ser usado quando se refere a mesma variavel
        else:
            impar += 1
print('Voce digitou {} números pares e {} números ímpares! '.format(par, impar))
