num = int(input('Digite um número inteiro'))
print('''Escolha uma das bases para conversão:
[ 1 ]conversão para BINÁRIO
[ 2 ] conversão para OCTAL
[ 3 ] conversão para HEXADECIMAL ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Biinário é igual : {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Biinário é igual : {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Biinário é igual : {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')
