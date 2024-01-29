vel= float(input('qual a velocidade do carro? '))
if vel<=80:
    print('Tenha um bom dia e dirija com segurança')
else:
    print('MULTADO!, você estava {}km/h acima do limite de velocidade e deverá'
          'pagar um multa de {:.2F}R$'.format(vel-80, (vel-80)*7))
