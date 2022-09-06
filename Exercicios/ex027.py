"""Faça um programa que leia o nome completo de uma pessoa, mostrando um seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza"""

nome = str(input('Digite o nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é "{}".'.format(n[0]))
print('Seu último nome é "{}".'.format(n[len(n)-1]))
print('Seu nome tem {} caracteres.'.format(len(nome) - nome.count(' ')))

