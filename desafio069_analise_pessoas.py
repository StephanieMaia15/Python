cont18 = m = f = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (m-masculino,f-feminino): ')).lower()
    if idade > 18:
        cont18+=1
    if sexo == 'm':
        m +=1
    if sexo == 'f' and idade < 20:
        f+=1
    option = str(input('Deseja continuar (s-sim, n-não) -> ' ))
    if option == 'n':
        break

print(f'''\n->Neste grupo foram contabilizadas {cont18} com mais de 18 anos.

->Foram identificados {m} homem(s).

->Foram identificadas {f} mulher(s) com menos de 20 anos.\n''')
