from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
anoat = date.today().year

print('quem nasceu em {} tem {} em {}'
      .format(ano, anoat - ano, date.today().year))
if date.today().year- ano == 18:
    print('vá se alistar IMEDIATAMENTE')
elif date.today().year -ano>18:
    print('você deveria ter se alistado a {} anos em {}'
          .format(anoat-ano-18, ano+18))
elif date.today().year - ano<18:
    print('Seu alistamento será em {}'.format(ano+18))
