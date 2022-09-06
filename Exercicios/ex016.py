# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Crie um programa que leia um número real qualquer e arredonde seu valor para cima e para baixo.

import math
num = float(input('Entre com um valor: '))
print('O número {}, arredondado para cima é o número {}.'.format(num, math.ceil(num)))
print('O número {}, arrendodado para baixo é o número {}.'.format(num, math.floor(num)))
print('A porção inteira do número {} é o número {}.'.format(num, math.trunc(num)))
print('A porção inteira do número {} é o número {}.'.format(num, int(num)))


