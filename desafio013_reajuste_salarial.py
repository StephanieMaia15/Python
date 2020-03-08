salario = float(input('Qual o salário do funcionário? '))
reajuste = float(input('Qual o valor em porcentagem para aumento? '))
valor_reajustado = salario + (salario * reajuste / 100)
print('O salário de R$ {:.2f} , com reajuste de {:.0f}% passou a ser R$ {:.2f} '.format(salario, reajuste, valor_reajustado))
