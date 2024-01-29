frase = input('Digite uma frase: ').strip()
print('A letra "A" aparece {} vezes \na primeira letra "A" apareceu na posição {}\n'
      'a última letra "A" apareceu na posição {}'
      .format(str.count(frase.lower(), 'a'),
              str.find(frase.lower(), 'a')+1,
              str.rfind(frase.lower(), 'a')+1))