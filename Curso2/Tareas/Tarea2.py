fname = input("Digite nombre del archivo: ")
fh = open(fname)

for texto in fh:
    texto=texto.rstrip()
    print(texto.upper())
