dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos kilometros foram rodados? '))
print('Total a pagar é R${:.2f}'.format(dia*60+km*0.15))
