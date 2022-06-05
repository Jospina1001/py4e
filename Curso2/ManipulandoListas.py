#suma de listas
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)

#cortar cadenas
print(c[1:3])
print(c[:4])
print(c[3:])
print(c[:])

#construir una lista
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

#saber si hay algo en la lista x in list
if 99 in stuff:
    print(True)

if 999 not in stuff:
    print(True)

if 100 in stuff:
    print(True)
else:
    print(False)

#ordenar listas
friends = ['Juan','Alejandro','Diego']
friends.sort()
print(friends)

#mas funciones
nums = [3,41,12,9,74,15]
print(len(nums)) #cantidad de datos
print(max(nums)) #numero mas grande
print(min(nums)) #numero mas pequeño
print(sum(nums)) #suma de numeros
print(sum(nums)/len(nums)) #promedio
print(nums[2:4])
