# O mesmo profssor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
nome1 = str(input('Nome: '))
nome2 = str(input('Nome: '))
nome3 = str(input('Nome: '))
nome4 = str(input('Nome: '))
list = [nome1, nome2, nome3, nome4]
random.shuffle(list)
print('A ordem de apresentação é {}.'.format(list))

