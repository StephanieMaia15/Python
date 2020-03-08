# Verificando qual é o menor número digitado
a = int(input('Digite o primeiro numero:'))
b = int(input('Digite o segundo numero:'))
c = int(input('Digite o terceiro numero:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor numero é: {} '.format(menor))


