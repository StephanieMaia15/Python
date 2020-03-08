#realizando a analise de 4 pessoas retornando algumas amostras.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('--------{}˚ pessoa:'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm:':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('A idade do homem mais velho é {} anos e ele se chama {}'.format(maioridadehomem, nomevelho))
print('O total de mulheres com menos de 20 anos é: {}'.format(totmulher20))
