import random
vit = 0
while True:
    v = int(input('Diga um valor: '))
    pi = input('Par ou impar [P/I]: ').upper()
    pc = random.randint(1, 9)
    if pi == 'P':
        if (v+pc)%2 == 0:
            vit+=1
            print('Você Venceu, o computador escholheu {} e você {} '
                  .format(pc, v))
        else:
            print('Você perdeu!, o computador escholheu {} e você {} '
                  .format(pc, v))
            break
    elif pi == 'I':
        if (v+pc)%2 != 0:
            vit+=1
            print('Você Venceu, o computador escholheu {} e você {} '
                  .format(pc, v))

        else:
            print('Você perdeu!, o computador escholheu {} e você {} '
                  .format(pc, v))
            break
print('GAME OVER, você ganhou {} vezes consecutivas'.format(vit))