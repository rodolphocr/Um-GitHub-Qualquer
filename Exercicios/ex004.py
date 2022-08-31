#COMO SABER O TIPO DE UMA VARIAVEL
from goto_py import goto
valor = input('Digite valor: ')
print('O tipo primitivo desse valor e. {}', type(valor))
print('Só tem espacos? {}.'.format((valor.isspace())))
print('Está em MAIUSCULA? {}.'.format(valor.isupper()))
print('Esta em minuscula? {}.'.format(valor.islower()))
print('Valor e numerico? {}.'.format(valor.isnumeric()))
print('Valor e alfanumerico? {}.'.format(valor.isalnum()))
print('Valor e alfabetico? {}.'.format(valor.isalpha()))
print('Valor e titelizado? {}.'.format((valor.istitle())))
goto(3)

