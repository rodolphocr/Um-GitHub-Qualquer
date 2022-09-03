#ESCREVA UM PROGRAMA QUE LEIA O VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS.
num = float(input('Entre com o valor em metros para converte-lo em centimetros e milimitros: '))
cm = (num * 100)
print('{} M transformado em CM é {};'.format(num, cm))
mm = (num * 1000)
print('{} M transformado em MM é {};'.format(num, mm))