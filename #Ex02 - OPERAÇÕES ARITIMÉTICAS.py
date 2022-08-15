# Tipos Primitivos e Saída de Dados

# + Adição / # - Subtração / # * Multiplicação / # / Divisão /  # ** Potência / # // Divisão Inteira / # % Resto da Divisão / # == Igual


# SOMA DE 2 NÚMEROS(inteiros_"int") E MOSTRAR O RESULTADO.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
resultado = n1 + n2
print('Resultado da soma é : ', resultado)

# SOMA DE 2 NÚMEROS(reais_"float") E MOSTRAR O RESULTADO.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
resultado = n1 + n2
#print('Resultado da soma é : ', resultado)
print('Resultado da soma {}'.format(resultado))

# DESCOBRIR QTOS ANOS A PESSOA TEM.
ano_nascimento = int(input('Entre com o ano que você nasceu: '))
ano = (2022)
idade = ano - ano_nascimento
print('Você tem {} '.format(idade))

#DESCOBRIR O ANTESSOR E SUCESSOR DE UM NÚMERO
n=int(input('Entre com o número :'))
s=n + 1
a=n - 1
print('O sucessor de {} é {} e o antessor é {}'.format(n, s, a))

#TABOADA
n=int(input('Entre com um número para calcular a taboada: '))
print('---- TABOADA do: ', n,  '------')
print(n,'x 1 = ', n *1)
print(n,'x 2 = ', n * 2)
print(n,'x 3 = ', n * 3)
print(n,'x 4 = ', n * 4)
print(n,'x 5 = ', n * 5)
print(n,'x 6 = ', n * 6)
print(n,'x 7 = ', n * 7)
print(n,'x 8 = ', n * 8)
print(n,'x 9 = ', n * 9)
print(n,'x 10 = ', n * 10)

#CALCULAR A CONVERSÃO DE REAL EM DOLAR
d=int(input('Qto de dinheiro você tem na carteira em real? '))
dolar=float(3.27)
resultado=(d * dolar)
print('Você pode comprar com', d, 'reais', resultado, 'dolares')



