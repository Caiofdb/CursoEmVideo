h=str()
mulher = 0
velho=0
media= float()
for i in range(1,5):
    print('-'*4,'{}ª'.format(i),'-'*4)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ').upper()
    media+=idade
    if sexo == 'M' and idade>velho:
        h=nome
        velho=idade
    if sexo== 'F':
        mulher+=1
print('a média de idade do grupo é {:.1f} anos\n O homem mais velho é {}, '
      'e tem {}anos \n Ao todo são {} com menos de 20 anos'
      .format(media, h, velho, mulher))