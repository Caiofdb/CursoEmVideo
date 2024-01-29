from math import sqrt, pow
co = float(input("Digite o cateto oposto: "))
ca = float(input('Digite o cateto adjacente: '))
print('A hipotenusa vai medir {}'
      .format(sqrt(pow(co, 2)+pow(ca, 2))))
# math.hypot(co, ca)