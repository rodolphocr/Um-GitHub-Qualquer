"""Faça um programa que leia uma frase pelo teclado e mostre:
 1 - Quantes vezes aparece a letra "A".
 2 - Em que posição ela aparece a primeira vez.
 3 - Em que posição ela aparece a última vez."""

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase digitada.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
