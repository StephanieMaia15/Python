#Verificando se um aluno atingiu a nota necessária para passar de ano
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nota = (n1 + n2) / 2
if nota < 5:
    print('{} Reprovado! '.format(nota))
elif 7 > nota >= 5:
    print('{} Recuperação!'.format(nota))
elif nota >= 7:
     print('{} Aprovado! '.format(nota))

