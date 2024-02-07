peso = float(input('digite seu peso: '))
h = float(input('digite sua altura: '))
imc = peso/(h**2)
print('seu imc é ', imc)
if imc<18.5:
    print('você está abaixo do peso')
elif 25>imc>=18.5:
    print('você está no peso ideal')
elif 30>imc>=25:
    print('você está com sobre peso')
elif 40>imc>=30:
    print('você está obeso')
elif imc>=40:
    print('você está com obesidade morbida')
