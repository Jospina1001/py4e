#de cadena a lista
abc = "with tree words"
stuff = abc.split()
print(stuff)

for w in stuff:
    print(w)

#este split divide segun espacios
#entonces busca los espacios en blanco y corta
#cuando no esta dividido por espacios puede ser un problema
#para eso le damos un parametro a split, que es decir donde cortar

line = "A lot of            spaces"
etc = line.split()
print(etc)

line = "hola.a.todos"
thing = line.split()
print(thing)

#como vemos, no corta si estan separados por puntos u otro objeto
#asi que...
thing = line.split('.')
print(thing)
