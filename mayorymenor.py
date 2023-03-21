num1 = int(input('Ingrese primer número: '))
num2 = int(input('Ingrese segundo número: '))

if num1 > num2:
    print(f'El numero {num1} es mayor al número {num2}')
elif num2 > num1:
    print(f'El número {num2} es mayor al número {num1}') 
else:
    print('Los dos números son iguales')       