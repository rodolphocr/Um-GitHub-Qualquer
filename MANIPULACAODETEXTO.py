'''Manipulação de texto.'''

frase = str('Alibaba e os 40 ladrões da Sapucai do Sul')
print(frase)

#FATIAMENTO DE TEXTO
print(frase[0])  #Mostra o caractere 9
print(frase[9:13])  #Mostra o caractere 9 até o 12
print(frase[9:21:2])  #Mostra do 9 ao 21 pulando de 2 em 2
print(frase[:5])  #Mostra do 0 até o 4
print(frase[3:])  #Mostra do 3 até a último caractere
#------------------------------------------------------------------------------

#ANALISE DA FRASE
print(len(frase))  #conta o comprimento da frase com os espaços.
print(frase.count('o'))  #conta o número de letras 'o'(em minusculo)
print(frase.count('o', 0, 13))  #conta o número de ‘o’(em minusculo) de 0 até 12
print(frase.find('deo'))  #encontra onde tem o primeiro 'deo'
print('curso' in (frase))  #se encontrar a palavra sugerida escreve TRUE, caso não escreve FALSE - case sensitive

#print(dir(frase)) #mostra quais modulos podem ser usados na string.

#------------------------------------------------------------------------------

#Transformação
print(frase.replace('Python', 'Android'))  #vai substituir Python por Android
print(frase.upper())  #coloca toda a frase em maiúsculo.
print(frase.lower())  #coloca toda a frase em minúsculo.
print(frase.capitalize())  #deixa somente a primeira letra da string em maiúsculo.
print(frase.title())  #deixa a primeira letra de todas as palavras em maiúsculo.
print(frase.strip())  #elimina todos os espaços no início e no fim.
print(frase.rstrip())  #elimina todos os espaços da direita.
print(frase.lstrip())  #elimina todos os espaços da esquerda.
print(frase.join(frase))  #O método join() retorna uma string concatenada com os elementos de iterable

#------------------------------------------------------------------------------

#Divisão
print(frase.split())  #cria uma divisão onde na string onde tem espaço. E cada separação é recomeçada a contagem. Cria uma lista.

#------------------------------------------------------------------------------

#Junção
print('-'.join(frase)) #substitui os espaços da grase pelo caractere informado.

#Inversão de uma string
print(frase[::-1]) #escreve a frase ao contrário.

#------------------------------------------------------------------------------
print(frase.center(50, '+' )) # coloca + na frente e no final do texto
