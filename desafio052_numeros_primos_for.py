#numero divido por 1 ou por ele mesmo com o valor restante sendo inteiro:Ex 5 é divisível por 1 e 5 somente
num = int(input('Digite um número:'))
total = 0 #vai contar o numeros de vezes que o valor foi dividido
for c in range(1, num +1):
    if num % c == 0: # comando: se o resto da divisao do numero pelo contador for igual a 1
        print('\33[33m', end='')
        total += 1 # quantidade de divisoes onde o resultado nao é numero inteiro: vermelho
    else:
        print('\33[31m', end='') ## quantidade de divisoes onde o resultado é numero inteiro: amarelo
    print('{} '.format(c), end='')
print('\n\33[mO numero {} foi divisível {} vezes. '.format(num, total))
if total == 2: #Se o total da divisao for igual a 2 ele é divisivel
    print('E por isso ele é PRIMO! ')
else:
    print('E por isso ele não é PRIMO! ')

