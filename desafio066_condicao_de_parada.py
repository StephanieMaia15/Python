n = s = cont = 0
while True:
    n = int(input('Digite um número para somar (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores foi: {s}')
