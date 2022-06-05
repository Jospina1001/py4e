#imprimir archivo de texto
xfile = open('Prueba.txt')
for prueba in xfile:
    print(prueba)

#numero de lineas de archivo de texto
count  =0
cfile = open('Prueba.txt')
for line in cfile:
    count = count +1
print("numero de lineas:",count)

#leer todo el archivo
rfile = open('Prueba.txt')
inp = rfile.read()
print(inp)

#eliminar los espacios en blanco (problema ejercicio comienzo del programa)
pfile = open('Prueba.txt')
for space in pfile:
    space=space.rstrip()
    print(space)
