from random import shuffle
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input(', segundo aluno: ')
al3 = input(', terceiro aluno: ')
al4 = input(', quarto aluno: ')
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))