# ABAIXO TEMOS UM CÓDIGO QUE CONVERTE KM EM MILHAS.
# FOI DECLARO A VARIAVEL EM TIPO 'FLOAT', PARA QUE POSSAMOS COLOCAR NÚMEROS REAIS EX.: 4.25KM.
# FOI USADO O PRINT PARA MOSTRAR O RESULTADO NA TELA.

# CALCULAR CONVERSÃO DE KM PARA MILHA.
km = float(input('Entre com os KM: '))
milhas = float(1.609)
result = km / milhas
print('KM convertido em milhas são: ',result)

# CALCULAR A CONVERSÃO DE REAL EM DOLAR
d=float(input('Qto de dinheiro você tem na carteira em real? R$ '))
dolar=float(3.27)
resultado=(d  / dolar)
print('Você pode comprar com {} reais {:.2f} dolares'.format(d, resultado))
# print('Você pode comprar com', d, 'reais', resultado, 'dolares')

# CALCULAR QTOS LITROS DE TINHA SÃO PARA PINTAR UMA PAREDE
altura = float(input('Metros em altura: '))
largura = float(input('Metro em largura: '))
area = (altura * largura)
print('A parede tem {}m²'.format(area))
tinta = (area / 2)
print('Para pintar essa parede você vai precisar de {}L de tinta!'.format(tinta))
if tinta > 10:
    print('Precisamos comprar mais tinha.')
else:
    print('Temos tinha suficiente no estoque.')

#Faça um Programa que pergunte qual o seu salário no mês e divida pra saber quanto ganha por semana, por dia, por hora.
salario_mensal = float(input('Qual o salário recebio no mês: '))
semana = (salario_mensal / 4)
print('Seu salário por semana e de R${:.2f}.'.format(semana))
dias = (semana / 30)
print('Seu salário por dia é de R${:.2f}.'.format(dias))
horas = (dias / 8)
print('Seu salário por horas trabalhadas é de R${:.2f}'.format(horas))