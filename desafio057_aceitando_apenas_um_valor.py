while True:
    sexo = str(input('Informe o seu sexo: '))
    if sexo in 'MFmf':
        print('Próximo: ')
    else:
        print('Tente novamente')
