#fazendo a leitursa de 6 numeros. Identificando quais sao pares e realizando a soma deles.
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Os informou {} numeros pares e a soma deles é: {} '.format(cont, s))
