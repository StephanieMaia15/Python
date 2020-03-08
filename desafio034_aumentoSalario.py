#Calculando o aumento do salario de um funcionario de acordo com a porcentagem recomendada
salario = float(input('Digite o salário do funcionário: R$ '))
if salario <= 1250:
    aum = salario + (salario * 0.15)
else:
    aum = salario + (salario * 0.10)
print('O novo valor é de: R$ {}'.format(aum))