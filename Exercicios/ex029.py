'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80KM/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custa R$7.00 por cada Km acima do limite.'''
'''Para utilizar biblioteca "random'' é nessário importa-la'''

import random
'''Centralização do texto "placa_radar" '''
placa_radar = str(' RADAR DE VELOCIDADE A FRENTE ')
print(placa_radar.center(50, '='))

'''Centralização do texto "speedy_board" '''
speedy_board = str('Velocidade máxima a pista sã́o 80km/h')
print(speedy_board.center(61, '*'))

'''Utilizando a biblioteca random para gerar a velocidade do carro.'''
speedy = (random.randrange(1, 80))
speedy_car = int(speedy)
speedy_excedente = (speedy_car * 2)
speedy_information = ('Você passou à "{}km/h".'.format((speedy_excedente)))
print(speedy_information.center(50, '+'))

'''Calculo da velocidade excedente.'''
if speedy_excedente > 80:
    

