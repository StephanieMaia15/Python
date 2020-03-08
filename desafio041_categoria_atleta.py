#Identificando a qual categoria o atleta pertence de acordo com o ano de nascimento
from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('A idade do atleta é: {} '.format(idade))
if idade <= 9:
    print('O atleta tem {} anos e pertence a categoria Mirim.'.format(idade))
elif idade <= 14:
    print('Esse atleta tem {} anos e pertence a categoria Infantil.'.format(idade))
elif idade <= 19:
    print('Esse atleta tem {} anos e pertence a categoria Júnior.'.format(idade))
elif idade == 20:
   print('Esse atleta tem {} anos e pertence a categoria Sênior.'.format(idade))
else:
    idade >= 21
    print('Esse atleta tem {} e pertence a categoria Master.'.format(idade))
