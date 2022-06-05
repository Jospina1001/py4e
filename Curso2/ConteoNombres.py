nombre = dict()
while True:
    entrada = input("digite nombre: ")
    if entrada == 'done':
        break
    else:
        nombre[entrada] = nombre.get(entrada,0) + 1 #[1]
print(nombre)

#[1]: es como poner la siguiente linea de codigo:

#if entrada in nombre:
    #nombre[entrada] = nombre[entrada] + 1
#else:
    #nombre[entrada] = 1
