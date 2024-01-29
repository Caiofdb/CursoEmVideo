nome = input('Insira seu nome: ')
print(str.replace(nome, ' ', ''))
print('Em letras maiusculas: {}\n Em letras minusculas: {}\n'
     'tem {} letras ao todo\n seu primeiro nome é {} e tem {} letras.'
      .format(str.upper(nome), str.lower(nome),
              str.replace(nome, ' ', '').__len__(),
              str.split(nome)[0], str.split(nome)[0].__len__()));

