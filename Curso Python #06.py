
# SOMA DE 2 NÚMEROS + MENSAGEM DE RESPOSTA + SAÍDA DE RESULTADO
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite um número: '))
# resultado = n1 + n2
# print('A SOME ENTRE',  n1,  'e ',  n2, 'VALE ', ':', resultado)
# print("A Soma entre {0} e {1} vale {2}".format(n1, n2, resultado))

# MOSTAR O TIPO DA VARIAVEL
# n=input('Digite um valor: ')
# print(type(n))

# dia=input('Dia =')
# mes=input('Mês =')
# ano=input('Ano =')
# print('Você nasceu no dia', dia, 'de', mes, 'de', ano,'. Correto?')

# primeiro=int(input('Entre com o primeiro número: '))
# segundo=int(input('Entre com o segundo número: '))
# soma=(primeiro) + (segundo)
# print('Resultado: ', soma)

#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o segundo número: '))

if n1 > n2:
    print('O maior número informado é {}'.format(n1))
else:
    print('O maior número informado é {}'.format(n2))

#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = str(input('Entre com a letra F para Feminino or M para Masculino: '))
if letra == 'F':
    print('FEMININO')
if letra == 'M':
    print('MASCULINO')
elif letra != 'F' and 'M':
    print('Sexo Inválido.')

# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# Comando exit(), é uma função que termina um outro comando ou finaliza um programa ou função.
materia = str(input('Entre com a matéria de referencia: '))
nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
soma = (nota1 + nota2)
media = (soma / 2)
print('Sua média é {}.'.format(media))
while media == 10:
    print('Aprovado com distinção na máteria de {}.'.format(materia))
    exit()
if media < 7:
    print('Reprovado na matéria de {}, estude mais.'.format(materia))
elif media >= 7:
    print('Você foi aprovado na máteria de {}.'.format(materia))