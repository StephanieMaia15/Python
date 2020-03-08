frase = ('  Curso em Vídeo Python')
print(frase[3:]) #posicao 3 ate o final
print(frase.count('o')) #conta quantos 'o' tem na frase
print(frase.upper().count('O')) #joga as palavras para maiuscula e conta quantos Os tem na frase
print(len(frase.strip())) #tamanho da frase e o strip para eliminar espacos desnecessarios
print(frase.find('Vídeo')) #encontrando a palavra dentro da frase
print(frase.lower().find('vídeo')) #transformando em minuscula e depois localizando a palavra dentro da frase
frase = frase.replace('Python', 'Android') #substituindo a palavra Python para Android
print(frase)
print(frase.split()) #dividindo as palavras
dividido = frase.split() #variavel
print(dividido[0]) #pegando a primeira palavra da separacao
print(dividido[2][3]) #pega a palavra na posicao dois e me mostre a letra na posicao 3
