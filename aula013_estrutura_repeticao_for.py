#estrutura de repaticao usando FOR
for c in range(1, 6): #contando de um ate 5
    print('Oi') # vai repetir a palavra oi 5 vezes
n = int(input('Digite um número: '))
for c in range(0, n+1): #pega o ultimo + um
    print(c) # vai ler o número contando de 0 ate o valor digitado
print('Fim')
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo: '))
for c in range(i, f+1, p): #ler o numero, o ultimo mais 1 a quantidade para pular
    print(c)
print('Fim')
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # somando 0 mais os valores digitados
print('\33[4:mA soma dos valores é: {} '.format(s))