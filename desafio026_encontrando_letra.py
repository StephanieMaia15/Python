frase = str((input('Digite uma frase: ')).upper().strip()) # jogando pra maiuscula e removendo espacos
print(frase.count('A'))
print(frase.find('A')+1) # pegando a posicao zero + 1
print(frase.rfind('A')+1) #pegando a ultima posicao + 1
