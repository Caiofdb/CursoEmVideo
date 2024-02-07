n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1+n2)/2
if m>=7:
    print('Aprovado com média ', m)
elif m<7 and m>=5:
    print('nota {} insuficiente você está em recuperação'.format(m))
elif m<5:
    print('nota {} insuficiente vc está reprovado'.format(m))