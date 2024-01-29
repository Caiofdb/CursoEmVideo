dis = float(input('Qual a distancia da sua viagem? '))
print('Sua viagem tera {}km'.format(dis))
if dis <= 200:
    print('sua viagem custará {:.2f}R$'.format(dis*.5))
else:print('sua viagem custará {:.2f}R$'.format(dis*.45))