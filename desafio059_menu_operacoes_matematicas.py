#Gerando loop de operacoes matematicas enquanto solicitado pelo usurio
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = (int(input('''
O que deseja fazer?\n[1] SOMAR\n[2] Multiplicar \n[3] Mair\n[4] Menor\n[5] Sair''')))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos dois números foi: {}'.format(soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação dos dois números foi: {}'.format(mult))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que {} '.format(n1, n2))
        else:
            menor = n1
            print('O número {} é maior que {} '.format(n2, n1))
    elif opcao == 4:
        if n1 < n2:
            print('O número {} é menor que {} '.format(n1, n2))
        else:
            menor = n2
            print('O número {} é menor que {} '.format(n1, n2))

    elif opcao == 5:
         print('Processo finalizado!')

