from datetime import date
ano = int(input('Digite o ano do seu nascimento:'))
atual = date.today().year
idade = atual - ano
if idade < 18:
    saldo = 18 - idade
    print('Com {}, você ainda não precisa se alistar. Ainda tem {} ano(s) para fazer isso.'.format(idade, saldo))
    anoAlistamento = atual + saldo
    print('Seu alistamento será em {} :'.format(anoAlistamento))

elif idade == 18:
    print('Com {}, esta na hora de se alistar!'.format(idade))

elif idade > 18:
    saldo = idade - 18
    print('Com {} anos, já deveria ter se alistado a {} anos atrás !'.format(idade, saldo))
    anoAlistamento = atual - saldo
    print('O seu alistamento deveria ter sido em {}'.format(anoAlistamento))


