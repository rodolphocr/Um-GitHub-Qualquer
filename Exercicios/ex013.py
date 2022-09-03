#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''salario = float(input('Entre com o valor do salário: '))
porc = int(15)
aumento= salario + (salario * porc / 100)
print('Você ganhou 15% de aumento no seu salario de R${}, totalizando R${:.2f}.'.format(salario, aumento))'''

salario = float(input('Entre com o valor do salário R$: '))
porc15 = int(15)
porc10 = int(10)
porc05 = int(5)

if salario >= 10000:
    valor_agreg = salario + (salario * porc05 / 100)
    print('Salarios acima de R$10.000, recebem {}% de aumento.'.format(porc05))
    print('Salário atual R${}.'.format(salario))
    print('Salario com aumento R${}'.format(valor_agreg))
elif salario == 7500:
    valor_agreg = salario + (salario * porc10 / 100)
    print('Salarios em carteira de R$7.500, recebem {}% de aumento.'.format(porc10))
    print('Salario atual R${}.'.format(salario))
    print('Salario com aumento R${}.'.format(valor_agreg))
else:
    valor_agreg = salario + (salario * porc15 / 100)
    print('Salario em carteira abaixo de R$7.500, recebem {}% de aumento.'.format(porc15))
    print('Salario atual R${}.'.format(salario))
    print('Salario com aumento R${}.'.format(valor_agreg))


