# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO é de {:.2f}.'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO é de {:.2f}.'.format(angulo, cosseno))
tangente = math.tan((math.radians(angulo)))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))
