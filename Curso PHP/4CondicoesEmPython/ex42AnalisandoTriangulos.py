l1 = float(input('Informe o lado1 do triângulo'))
l2 = float(input('informe o lado2 do triângulo'))
l3 = float(input('informe o lado3 do triângulo'))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    if l1==l2==l3:
        print('Triângulo Equilatero')
    elif l1==l2 or l1==l3 or l2==l3:
        print('Triângulo isoceles')
    else:
        print('Triângulo escaleno')
else:
    print('isso não é um triângulo')