"""''''ORDEM DE PRECEDENCIA DOS OPERADORES ARITIMÉTICOS.''''"""

'''
Primeiro é executado tudo que estiver dentro dos parentes. ( )
Segundo é executado a (** potência)
Terceiro  é executado  (* multiplicação)  (/ divisão) (// divisão inteira) (% resto da divisão)
Quarto é executo (+ adição) (- subtração) 
'''
from goto_py import goto
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = (n1 + n2)
s = (n1 - n2)
m = (n1 * n2)
d = (n1 / n2)
p = (n1 ** n2)
di = (n1 // n2)
print('A soma e {}, a subtracao {}, a multiplicao {}, a divisao {:.2f}, a potencia e {}, \ne a divisao por numero inteiro {}.'.format(a, s, m, d, p, di))
goto(9)

