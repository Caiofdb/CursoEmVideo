import datetime
nas = int(input('Informe nascimento do atleta'))
idade = datetime.date.today().year - nas
print('o atleta tem {} anos'.format(idade))
if idade<=9:
    print('Atleta Mirim')
elif idade>9 and idade<=14:
    print('Atleta infantil')
elif idade>14 and idade<=19:
    print('Atleta juvenil')
elif idade>19 and idade<=25:
    print('Atleta Senior')
elif idade>25:
    print('Atleta Master')
