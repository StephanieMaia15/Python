dias = int(input('\033[7;33mQual a quantidade de dias que o carro foi locado? \033[m'))
q_km = float(input('Quantos KM rodados no total?'))
pagar =(dias * 60) + float((q_km * 0.15))
print('O total a pagar é : {}'.format(pagar))
