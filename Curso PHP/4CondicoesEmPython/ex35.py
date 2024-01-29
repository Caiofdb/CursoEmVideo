l1 = float(input('digite em ordem 3 segmentos de reta e verificarei '
                 'se podem formar um triângulo: '))
l2 = float(input())
l3 = float(input())
if (l1+l2>l3 and l1+l3>l2 and l2+l3>l1 and
        (l1-l2 or l2-l1)<l3 and (l1-l3 or l3-l1)<l2 and (l2-l3 or l3-l2)<l1):
    print('os segmentos {}, {}, {} podem formar um triângulo'
          . format(l1, l2, l3))
else:
    print('os segmentos {}, {}, {} não podem formar um triângulo'
          . format(l1, l2, l3))