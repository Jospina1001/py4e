#operador index
fruit = 'banana'
letter = fruit[1]
print(letter)
#segunda parte de ejemplo
x = 3
w = fruit[x-1]
print(w)

#para obtener la longitud de la palabra se puede usar
#la funcion len
y=len(fruit)
print('la palabra',fruit,'tiene',y,'letras')

#ahora un loop para obtener todos lo caracrteres de
#una palabra, y cual es su digito correspondiente
fruit='banana'
index=0

print('Con while:')

while index<len(fruit):
    letras = fruit[index]
    print(index,letras)
    index=index+1

print('Con for:')

for letter in fruit:
    print(letter)

#podemos hacer que cuente cuantas letras hay en una frase
word='banana'
count=0
for letter in word:
    if letter == 'a':
        count=count+1
print('hay',count,'letras a')

#CORTE DE CADENAS
#sirve para cortar la cadena hasta donde queramos

s = 'Juan Ospina' #11 caracteres desde el 0 al 11
print(s[0:4])
print(s[5:11])
print(s[2:8])

#ojo si tomamos 0:4, decimos que tomamos el caracter 0,1,2,3 pero no el 4
#al igual que por ejempo 5:11, tomamos 5,6,7,8,9,10 pero no el 11
#si hacemos un valor que esta fuera del rango, no pasa nada
#tambien podemos eliminar el primer caracter o el ultimo de la cadena

print(s[:6])
print(s[8:])

#si solo dejamos : tomara toda la frase
print(s[:])
