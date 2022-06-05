#NO SON MODIFICABLES
#VERSION MAS LIMITADA DE LAS LISTAS
#ES IGUAL QUE LAS LISTAS PERO SE USAN () EN LUGAR DE []

x=('Gleen','Sally','Joseph')
print(x[2])

#Asignacion y tuplas
(x,y)=(5,99)
print(x)
print(y)


#podemos comparar tuplas

if (1,2,3)<(4,5,6):
    print('verdadero')
else:
    print('falso')

#empieza por izquierda y compara, si son iguales va al siguiente item
#y asi, todo esto solo lo hace si son iguales, de otro modo saca la conclusion

#diccionario con tuplas
d = {'a':10,'b':1,'c':22}
t = sorted(d.items())
for k,v in sorted(d.items()):
    print(k,v)

#ordenar un diccionario con tuplas
c ={'a':10,'b':1,'c':22}
tmp = list()
for k,v in sorted(d.items()):
    tmp.append((v,k))
print(tmp)

tmp=sorted(tmp, reverse=True)
print(tmp)
