#Tabuada
tabuada = float(input('Entre com o número que você deseja a tabuada: '))
print('====== Tabuada do {} ====== '.format(tabuada))
for count in range (10):
    r1 = (count + 1)
    r2 = (tabuada * r1)
    print('{} x {} = {}'.format(tabuada, r1, r2))
    #print('{} x {} = {}'.format(tabuada, count + 1, tabuada * (count +1 )))
