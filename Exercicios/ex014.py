# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit, Kelvin, Rankine,
# Réaumur, Romer, Newton e Delisle
# As principais unidades de temperatura em graus são: Celsius, Fahrenheit, Kelvin, Rankine, Réaumur, Romer, Newton e Delisle

def menu_inicial():
    print('Programa para conversão de Celsius para outras unidades de medidas de temperaturas.')
    print('1. Converter Celsius para Fahrenheit.')
    print('2. Converter Celsius para Kelvin.')
    print('3. Converter Celsisus para Rankine.')
    print('4. Converter Celsius para Reaumur.')
    print('5. Converter Celsisus para Romer.')
    print('6. Converter Celsius para Newton.')
    print('7. Converter Celsius para Delisle.')

def cel_fahr():
    print('===== Conversão de Celsius para Fahrenheit=====')
    print('Formula de Fahrenheit [°F] = [°C] × 9⁄5 + 32')
    celsius = float(input('Entre com o valor em Celsius: '))
    fahrenheit = (celsius * 9 / 5) + 32
    print('{}°C Celsius convertido para Fahrenheit são {}°F.'.format(celsius, fahrenheit))

def cel_kel():
    print('===== Conversão de Celsius para Kelvin =====')
    print('Formula de Kelvin [K] = [°C] + 273,15')
    celsius = float(input('Entre com o valor em Celsius: '))
    kelvin = float(273.15)
    conversao = (celsius + kelvin)
    print('{}°C Celsius convertido para Kelvin são {}°F.'.format(celsius, conversao))

def cel_rank():
    print('===== Conversão de Celsius para Rankine ===== ')
    print('Formula de Rankine [°R] = ([°C] + 273,15) × 9⁄5')
    celsius = float(input('Entre com o valor em Celsius: '))
    rankine = float(491.67)
    conversao1 = celsius * ( 9 / 5)
    conversao2 = (conversao1 + rankine)
    print('{}°C Celsius convertido para Rankine são {:.2f}°R.'.format(celsius, conversao2))

def cel_rea():
    print('===== Conversão de Celsius para Reamur ===== ')
    print('Formula de Reamur [°Ré] = [°C] × 4⁄5')
    celsius = float(input('Entre com o valor em Celsius: '))
    reamur = (celsius * 4 / 5)
    print('{}° Celsius convertido para Reamur {}°Re.'.format(celsius, reamur))

def cel_rom():
    print('===== Conversão de Celsius para Romer =====')
    print('Formula de Romer [°Ro] = [°C] × 21⁄40 + 7,5 ')
    celsius = float(input('Entre com o valor em Celsius: '))
    romur = (celsius * 21 / 40) + 7.5
    print('{}°C Celsius convertido para Romur são {}°Ro.'.format(celsius, romur))

def cel_new():
    print('===== Conversão de Celsius para Newton =====')
    print('Formula de Newnton [°N] = [°C] × 33⁄100')
    celsius = float(input('Entre com o valor em Celsius: '))
    newton = celsius * (33 / 100)
    print('{}°C Celsisus convertido para Newton são {:.2f}°N.'.format(celsius, newton))

def cel_deli():
    print('===== Conversão de Celsius para Delisle ===== ')
    print('Formula de Delisle [°De] = (100 − [°C]) × 3⁄2')
    celsius = float(input('Entre com o valor em Celsius: '))
    delisle = ( 100 - celsius) * 3 / 2
    print('{}° Celsius convertido para Delisle são {}°De.'.format(celsius, delisle))

if  __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o qual conversaõ você deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        cel_kel()

    if escolha == '3':
        cel_rank()

    if escolha == '4':
        cel_rea()

    if escolha == '5':
        cel_rom()

    if escolha == '6':
        cel_new()

    if escolha == '7':
        cel_deli()
