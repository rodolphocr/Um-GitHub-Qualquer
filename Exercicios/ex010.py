#CRIE UM PROGRAMA QUE LEITA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QTOS DÓLARES ELA PODE COMPRAR.
real = float(input('Qto você tem na carteira: '))
dolar = (real / 3.27)
print('Com R${} voce pode comprar US{:.2f}'.format(real, dolar))
