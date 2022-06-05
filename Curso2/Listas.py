#podemos usar variables "listas" para tener mas de un dato
x = [1,2,3]
print(x)

#podemos encapsular varios datos
colors = ['red','yellow','blue']
print(colors)

#e incluso combinar
y = ['red',6,98.6]
print(y)

#y poner otras listas
z = [0,x,5]
print(z)

#ya las hemos usado en sentencias for
for i in [5,4,3,2,1]:
    print(i)

#para mirar dentro de la lista usamos [], de forma que
#decimos en que posicion queremos averiguar el dato
#EMPEZANDO DESDE LA POSICION 0
friends = ['joseph','juan','esteban']
print(friends[1])

#y podemos cambiar los valores de las listas
x[2] = 4
print(x)

#funcion range: nos funciona para hacer una lista de x numeros, se usa para loops
#empieza desde 0
for j in range(5):
    print(j)
