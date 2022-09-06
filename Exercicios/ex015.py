# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

from goto_py import goto
marca = str(input('Entre com a marca do automovel: '))
modelo = str(input('Entre com o modelo do automovel: '))
kms = float(input('Quantos KMs rodados: '))
dias = int(input('Quantos dias alugados? '))
print('=================== Valores há pagar do aluguel de um {}, {}. ==================='.format(marca, modelo))
aluguel = float(60)
gasolina = float(0.15)
valor_gasolina = (kms * gasolina )
valor_dia = (dias * aluguel)
valor_total = (valor_gasolina + valor_dia)
print('O aluguel equivalente a {} KMs rodados e {} dias alugados, é de R${}.'.format(kms, dias,valor_total))
goto(5)
