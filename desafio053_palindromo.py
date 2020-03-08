#Palíndromo é quando uma palavra ou um conjunto de palavras é escrita e
# quando se le ao contrario ela forma a mesma palavra original
frase = str(input('Digite uma frase: ')).strip().upper() # solicitado um string de palavras, removido os espaçoes colocando tudo em maiúscula
palavras = frase.split() #separando as palavras (gerando uma lista)
junto = ''.join(palavras) #juntando as palavras da lista
inverso = '' #espaco vazio
for letra in range(len(junto)-1, -1, -1): #pegando a ultima letra ate a primeira e voltando de uma em uma
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo')

#para substituir o for podemos usar o seguinte comando:
#a variavel INVERSO passa a receber = junto [::-1]