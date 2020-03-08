#analisando a idade de 7 pessoas e calculando se elas sao maiores de idade ou nao
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}˚ pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('\33[33mAo todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('\33[36mE também tivemos {} pessoas menores de idade'.format(totmenor))
