#interrompendo While
n = s = 0
while True:
    n = int(input('Digite um número ou 999 para parar: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

#######Utilizando f string no lugar do .format
#ex: print(f'A soma vale {s}') == tecnica de interpulacao

nome = 'José'
idade = 33
print(f'O nome é {nome} e tem {idade} anos. ')

