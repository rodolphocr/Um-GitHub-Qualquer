"""Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúsculas.
2 - O nome com todas as letras minúsculas.
3 - Quantas letras ao todo (sem considerar espaços).
4 - Quantas letras tem a primeiro nome. """

nome = str(input('Entre com seu nome completo: ')).strip()
cap_nome = nome
print('Analisando nome que foi escolhido. . .')
print('Nome em MAIÚSCULO é "{}".'.format(cap_nome.upper()))
print('Nome em minúscolo é "{}".'.format(cap_nome.lower()))
print('O nome escolhido ao todo tem "{}" letras.'.format(len(cap_nome) - cap_nome.count(' ')))
print('O primeiro nome tem "{}" letras.'.format(cap_nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é "{}" e tem "{}" letras.'.format(separa[0], len(separa[0])))




