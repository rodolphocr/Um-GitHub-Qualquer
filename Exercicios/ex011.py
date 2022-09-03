# Faça um programa que leia a largura e a altura de
# uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de
# tinta pinta uma área de 2 metros quadrados.
from goto_py import goto
largura = float(input('Entre com a largura: '))
altura = float(input('Entre com altura: '))
area = (largura * altura)
print('Sua parede tem a dimensao de {}x{} e sua are e de {}m2.'.format(largura, altura, area))
tinta = (area / 2)
print('Para pintar essa parede, voce precisara de {}L de tinta.'.format(tinta))
goto(6)














































































