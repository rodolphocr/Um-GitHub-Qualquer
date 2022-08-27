#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
n1 = float(input('Entre com a nota do primeiro semestre: '))
n2 = float(input('Entre com a nota do segundo semestre: '))
soma_notas = (n1 + n2)
media = (soma_notas / 2)
if media >= 9.0 and media <= 10:
    print('Você tirou {} no primeiro semestre'.format(n1))
    print('Você tirou {} no segundo semestre'.format(n2))
    print(f'Sua media é \033[1;32m{media}\033[m')
    print('Você esta no conceito A, \033[7;1;4;32;40m(APROVADO)\033[m')
elif media >= 7.5 and media < 9:
    print('Você tirou {} no primeiro semestre.'.format(n1))
    print('Você tirou {} no segundo semestre.'.format(n2))
    print(f'Sua media é \033[1;32m{media}\033[m')
    print('Você esta no conceito B, \033[7;1;4;32;40m(APROVADO)\033[m')
elif media >= 6.0 and media < 7.5:
    print('Você tirou {} no primeiro semestre.'.format(n1))
    print('Você tirou {} no segundo semestre.'.format(n2))
    print(f'Sua media é \033[1;32m{media}\033[m')
    print('Você esta no conceito C, \033[7;1;4;32;40m(APROVADO)\033[m')
elif media >= 4.0 and media < 6.0:
    print('Você tirou {} no primeiro semestre.'.format(n1))
    print('Você tirou {} no segundo semestre.'.format(n2))
    print(f'Sua media é \033[1;31m {media}\033[m')
    print('Você esta no conceito D, \033[1;31m(REPROVADO)\033[m')
else:
    print('Você tirou {} no primeiro semestre.'.format(n1))
    print('Você tirou {} no segundo semestre.'.format(n2))
    print(f'Sua media é \033[1;31m{media}\033[m')
    print('Você esta no conceito E, \033[1;31m(REPROVADO)\033[m')

