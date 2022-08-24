#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.
from goto_py import goto
salario_hora = float(input('Qual o valor da hora trabalhada: '))
horas_trabalhada = int(input('Quantas horas trabalhadas: '))
salario_mensal = (salario_hora * horas_trabalhada)
ir = int(11)
inss = int(8)
sindicato = int(5)
print('\033[1mO salario bruto e de R$:\33[m \033[1;4;30;44m{}.\33[m'.format(salario_mensal))
salario_ir = salario_mensal - (salario_mensal * ir / 100)
print('\033[1mSalario descontando IR, R$:\33[m \033[1;4;30;41m{}\33[m'.format(salario_ir))
salario_inss = salario_ir - (salario_ir * inss / 100)
print('\033[1mSalario descontando IR e INSS. R$:\33[m \033[1;4;30;41m{:.2f}.\33[m'.format(salario_inss))
salario_sindicato = salario_inss - (salario_inss * sindicato / 100)
print('\033[1mSalario descontanto IR, INSS e Sindicato e de R$:\33[m  \033[1;4;30;41m{:.2f}.\33[m'.format(salario_sindicato))
print('\033[1mSalario liquido e de R$:\33[m \033[1;4;30;45m{:.2f}\33[m'.format(salario_sindicato))
goto(3)


