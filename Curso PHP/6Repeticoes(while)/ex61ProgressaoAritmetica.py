a1= float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são \n{}'.format(a1),end=' ')
cont = 2
while cont<=10:
    print('-> {}'.format(a1+r*(cont-1)),end=' ')
    cont += 1