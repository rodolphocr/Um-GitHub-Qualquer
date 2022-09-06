#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

#o quadrado da hipotenusa é igual a somo dos quadrados dos catetos H² = CV² + CH²

import math
co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))
result1 = (co ** 2)
result2 = (ca ** 2)
result3 = (result1 + result2) **(1/2)
print('O calculo da hipotenusa é {:.2f}'.format(result3))

hi = math.hypot(co, ca)
print('A hipotenusa é {:.2f}.'.format(hi))
