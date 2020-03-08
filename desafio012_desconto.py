preco_original = float(input('Digite o valor do produto R$ : '))
desconto = float(input('Digite o valor do desconto:'))
valor_desconto = preco_original -  (preco_original * desconto / 100)
print('O valor do produto com desconto de {:.0f}% é: R$ {:.2f}'.format(desconto, valor_desconto))
