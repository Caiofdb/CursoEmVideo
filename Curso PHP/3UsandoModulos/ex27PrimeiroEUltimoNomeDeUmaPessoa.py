nome = input('Digite seu nome completo: ').strip()
print('Prazer em te conhecer.\n'
      'Seu primeiro nome é {0}\n Seu ultimo nome é {1} '
      .format( nome.split()[0],
               nome .split()[nome.split().__len__()-1]))
