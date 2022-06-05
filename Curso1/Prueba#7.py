mayor=-1
menor=99999
suma=0

print('Digite 5 numeros')

numero1 = input('ingrese numero 1: ')
n1 = float(numero1)

numero2 = input('ingrese numero 2: ')
n2 = float(numero2)

numero3 = input('ingrese numero 3: ')
n3 = float(numero3)

numero4 = input('ingrese numero 4: ')
n4 = float(numero4)

numero5 = input('ingrese numero 5: ')
n5 = float(numero5)

for num in [n1,n2,n3,n4,n5]:
    if num > mayor:
        mayor=num
    if num< menor:
        menor=num
    suma=suma+num

print('El numero mayor fue: ',mayor)
print('El numero menor fue: ',menor)
print('La suma fue: ',suma)
