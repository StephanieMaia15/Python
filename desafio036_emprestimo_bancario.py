#Aprovando ou nao um emprestimo bancario
valor = float(input('Qual o valor da propriedade: '))
sal = float(input('Qual o seu salario mensal? '))
prazo = int(input('Por quantos anos sera pago ? '))
prestacao = valor / (prazo * 12)
condicao = sal * 0.30
aprovado = condicao % sal # pegando o que sobra do salario para fazer o cálculo
if prestacao <= condicao:
    print('O empréstimo será aprovado. O valor da prestaçao é: R${:.2f} '.format(prestacao))
else:
    print('Emprestimo negado! O valor R${:.2f} excede 30% da sua renda mensal'.format(prestacao))