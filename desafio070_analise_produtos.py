cont = total = totmil = menor = 0
barato = ''
while True:
    prod = str(input('Produto: '))
    valor = float(input('Preço: '))
    opcao = str(input('Deseja continuar: [S/N]').strip()).upper()
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = prod
    if opcao == 'N':
        break
    print('Cadastrado com sucesso!')

print(f'O total de produtos foi de {cont} unidades e o valor total é de R$ {total}')
print(f'O total de produtos acima de R$ 1000,00 foi de {totmil}')
print(f'O produto mais barato foi {barato} e custou R$ {menor}')
