a1= int(input('Primeiro termo da PA: '))
r= float(input('Razão da PA: '))
print('Os 10 Primeiros termos dessa PA são:')
for i in range(1,11):
    print('->',a1+(r*i),  end='')
