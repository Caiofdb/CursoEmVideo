import datetime
idade=int()
cont = 0
for i in range(1,8):
    idade = int(input('Digite o nascimento da {} ª pessoa: '.format(i)))
    if datetime.date.today().year - idade >=18:
        cont += 1
print('são {} pessoas maiores de idade \n'
      'e {} pessoas menores de idade'.format(cont, 7-cont))