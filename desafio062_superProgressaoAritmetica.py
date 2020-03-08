
print('Gerador de PA')
print(' - ' * 10) # linha de separacao opcional
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados '.format(total))
