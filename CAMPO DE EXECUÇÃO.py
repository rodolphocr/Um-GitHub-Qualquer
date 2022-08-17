# CALCULO DE DESCONTO EM REAIS.
# VARIÁVEL VALOR É O CALCULO DA PORCENTAGEM DO PREÇO
preco = float(input('Qual o preço do produto? R$ '))
porcento = int(input('Valor do desconto em %: '))
porcentagem = (preco * porcento / 100)
novo = (preco - porcentagem)
print('O produto que está no valor de R${}. \n'
'Com desconto de {}%, ficará R${}. '.format(preco, porcento, novo))

if novo > 800:
    print('Esse valor com desconto pode ser dividido em 10x no cartão e ficaria no valor de R${}.'.format(novo/10))