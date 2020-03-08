#para codigo ANSI (cor) no Python comeca com \033[tres valores: uma para estilo, um para texto e outro para fundo - termina com a letra m
#Style:
#0 = nada
#1 = bold
#4 = sublinhado
#7 = inversao
#-------------------------
#Text
#30 = branco
#31 = vermelho
#32 = verde
#33 = amarelo
#34 = azul
#35 = roxo
#36 = azul claro
#37 = cinza
#------------------------
#Back:
#para o fundo entre 40 a 47 segue a mesma ordem de cores do text

print('\033[0:30:41mOlá, Mundo\033[m')# removendo os espaços após o final da frase
print('\033[1:31:40mOlá, Mundo\033[m')
a = 10
b = 20
print('\033[32:43m{}\033[m e \033[33:44m {}\033[m '.format(a, b))
nome = 'Stephanie'
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))

