import math
ang = float(input('Digite o ângulo desejado: '))
print('o angulo de {} tem \n seno de {:.3f}\n'
      'cosseno de {:.3f} \n tangente de{:.3f}'
      .format(ang, math.sin(math.radians(ang)),
              math.cos(math.radians(ang)), math.tan(math.radians(ang))))
