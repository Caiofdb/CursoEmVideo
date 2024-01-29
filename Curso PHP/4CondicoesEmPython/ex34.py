sal = float(input('Qual seu sálario?'))
if sal<=1250:
    per = 1.15
else:
    per = 1.10
print('Quem ganhava {:.2f}R$ passará a ganhar {:.2f}R$'.format(sal,sal*per))