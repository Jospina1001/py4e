fname = input("Digite nombre del archivo: ")
fh = open(fname)
counts=dict()

for line in fh:
    words=line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1


bigword = 0
bigcount = 0

for word,count in counts.items():
    if bigcount == 0 or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)
