# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
nome1 = str(input('Entre com o primeiro nome: '))
nome2 = str(input('Entre com o segundo nome: '))
nome3 = str(input('Entre com o terceiro nome: '))
nome4 = str(input('Entre com o quarto nome: '))
list = [nome1, nome2, nome3, nome4]
escolhido = choice(list)
print('O Aluno escolhido foi {}.'.format(escolhido))

