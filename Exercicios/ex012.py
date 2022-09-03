#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Entre com o preço do produto: '))
valor = preco - (preco * 5 / 100)
print('Para esse valor de R${} é possível dar 5% de desconto ficando R${}.'.format(preco, valor))
