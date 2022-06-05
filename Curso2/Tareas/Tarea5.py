fname = input("Digite nombre del archivo: ")
fh = open(fname)

count=0

for line in fh:

    if line.startswith("From "):
        tx=line.split()
        print(tx[1])
        count=count+1

print("There were", count, "lines in the file with From as the first word")
