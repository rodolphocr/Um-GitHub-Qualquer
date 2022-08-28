# Formula para descobrir idadde:
from goto_py import  goto
nu_calcado = str(input('Entre o numero do seu sapato: '))
zero = str('00')
resultado = int(nu_calcado + zero)
ano_nascimento = int(input('Enter com o ano do nascimento: '))
resulado1 = int(resultado - ano_nascimento)
ano_atual = int(input('Entre como ano atual: '))
idade = int(resulado1 + ano_atual)
print('Os ultimos 2 digitos sao a sua idade {}'.format(idade))
goto(3)