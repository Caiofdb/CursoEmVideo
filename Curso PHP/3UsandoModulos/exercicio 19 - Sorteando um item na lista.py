import random
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input(', segundo aluno: ')
al3 = input(', terceiro aluno: ')
al4 = input(', quarto aluno: ')
lista = [al1, al2, al3, al4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))
