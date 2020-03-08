#calculando o valor a ser pago de acordo com a forma de pagamento
vatual = float(input('Digite o valor do produto: '))
print('''Formas de pagamento: 
[ 1 ] Dinheiro
[ 2 ] Débito à vista
[ 3 ] 2x Cartão de Crédito 
[ 4 ] 3x Cartão de Crédito''')
opcao = int(input('Qual a opção de pagamento? '))
if opcao == 1:
    total = vatual - (vatual * 10 / 100)
    print('O valor é de R${}'.format(total))
elif opcao == 2:
    total = vatual - vatual * 0.05
    print('O valor é R$ {}'.format(total))
elif opcao == 3:
    total = vatual / 2
    print('O valor de cada parcela é R$ {}'.format(total))
elif opcao == 4:
    total = (vatual + vatual * 0.20) / 3
    mais = vatual % total
    print('O valor é R$ {:.2f}. Acrescimo de {} reais'.format(total, mais))
else:
    print('Essa opção não esta disponível!')
