fname = input("Digite nombre del archivo: ")
fh = open(fname)

lst=list()

for line in fh:
    tx=line.split()

    for word in tx:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
