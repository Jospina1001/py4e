#CONCATENACION
a = 'hello'
b = a+ 'there'
print(b)

c = a+' '+'there'
print(c)

#IN como condicion fuera del for
fruit='banana'
if 'a' in fruit: #pregunta si hay una a en banana
    print('Found it')

#COMPARACION DE CADENAS
word='banan'

if word == 'banana':
    print('all right,bananas')

if word < 'banana':
    print('Your word,'+word+' comes before banana.')
elif word > 'banana':
    print('Your word,'+word+' comes after banana.')
else:
    print('all right,bananas')

#LIBERIA STRING

#quitar mayusculas
greet = 'HELLO BOB'
zap = greet.lower()
print(zap)
print('Hi There'.lower())

#hacer todo mayusculas
txt = 'hello bob'
nnn = txt.upper()
print(nnn)
print('Hi There'.upper())

#busqueda de letras

pos = fruit.find('na')
print(pos)
#nos devuelve un valor que es la posicion en donde esta el 'na'

aa = fruit.find('z')
print(aa)
#si no esta la letra, nos devuelve el valor de -1

#buscar y reemplazar

ejp = 'Hello Bob'
nstr = ejp.replace('Bob','Jane')
print(nstr)

nstr = ejp.replace('o','x')
print(nstr)

#WHITESPACE
greet = '     Hello Bob      '
a = greet.lstrip()#quita los espacios de la izquierda
print(a)
b = greet.rstrip()#quita los espacios de la derecha
print(b)
c = greet.strip()#quita los espacios de la derecha e izquierda
print(c)

#PREFIXES
#es para ver si una cadena empieza con cierta letra

line="Please have a nice day"
if line.startswith('Please'):
    print('Empieza con P mayuscula')
elif line.startswith('please'):
    print('Empieza con p minuscula')

#PARSING AND EXTRACTING
#es buscar y extraer

#informacion:
data = 'From juan.ospina02@correo.usa.edu.co Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
#primero buscamos el arroba

sppos = data.find(' ',atpos)
print(sppos)
#buscamos el espacio despues del correo

host=data[atpos+1:sppos]
print(host)
#y recortamos el correo
