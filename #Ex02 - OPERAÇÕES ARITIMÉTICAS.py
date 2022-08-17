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
print(n,'x 1 = ', n * 1)
print(n,'x 2 = ', n * 2)
print(n,'x 3 = ', n * 3)
print(n,'x 4 = ', n * 4)
print(n,'x 5 = ', n * 5)
print(n,'x 6 = ', n * 6)
print(n,'x 7 = ', n * 7)
print(n,'x 8 = ', n * 8)
print(n,'x 9 = ', n * 9)
print(n,'x 10 = ', n * 10)

# TABOADA
n = int(input('Entre com um número para calcular a taboada: '))
print('---- TABOADA do: ', n, '------')
print('{} x   {} = {}'.format(n, 1, n * 1))
print('{} x   {} = {}'.format(n, 2, n * 2))
print('{} x   {} = {}'.format(n, 3, n * 3))
print('{} x   {} = {}'.format(n, 4, n * 4))
print('{} x   {} = {}'.format(n, 5, n * 5))
print('{} x   {} = {}'.format(n, 6, n * 6))
print('{} x   {} = {}'.format(n, 7, n * 7))
print('{} x   {} = {}'.format(n, 8, n * 8))
print('{} x   {} = {}'.format(n, 9, n * 9))
print('{} x {} = {}'.format(n, 10, n * 10))

#TABOADA COM FOR COUNT IN.
tabuada=int(input("Tabuada do numero: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))

#CALCULAR A CONVERSÃO DE REAL EM DOLAR
d=int(input('Qto de dinheiro você tem na carteira em real? '))
dolar=float(3.27)
resultado=(d * dolar)
print('Você pode comprar com {} reais {} dolares'.format(d, resultado))
# print('Você pode comprar com', d, 'reais', resultado, 'dolares')

# CALCULANDO MÉDIAS DE NOTAS.
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
sn = nota1 + nota2
m = sn / 2
print('A média entre {} e {} é igual a {}'.format(nota1, nota2, m))

if m >=6:
    print('Sua média foi {} então você passou.'.format(m))
else:
    print('Sua média foi {} então você não passou.'.format(m))

# CALCULO DE DESCONTO EM REAIS.
# VARIÁVEL VALOR É A PORCENTAGEM DO PREÇO
preco = float(input('Qual o preço do produto? R$ '))
porcento = int(input('Valor do desconto em %: '))
porcentagem = (preco * porcento / 100)
novo = (preco - porcentagem)
print('O produto que está no valor de R${}. \n'
'Com desconto de {}%, ficará R${}. '.format(preco, porcento, novo))

if novo > 800:
    print('Esse valor com desconto pode ser dividido em 10x no cartão e ficaria no valor de R${}.'.format(novo/10))

