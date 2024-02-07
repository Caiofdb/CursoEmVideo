import random
from time import sleep
jogada = int(input('Suas opções\n[0]Pedra\n[1]Papel\n[2]Tesoura\nQual sua jogada? '))
escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
pc=random.choice([0,1,2])

if 3>jogada>=0:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('-=-'*8, '\nComputador jogou {}\nJogador jogou {}\n'
        .format(escolhas[pc], escolhas[jogada]),'-=-'*8)
if jogada == pc:
    print('EMPATE!!!')
elif (jogada==0 and pc==2) or(jogada==1 and pc==0) or (jogada==2 and pc==1):
    print('VITORIA')
elif (jogada==2 and pc==0) or(jogada==0 and pc==1) or (jogada==1 and pc==2):
    print('DERROTA')
else:
    print('Jogada invalida!')