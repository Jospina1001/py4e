fname = input("Digite nombre del archivo: ")
fh = open(fname)

counts=dict()

for line in fh:

    if line.startswith("From "):
        words=line.split()
        word=words[5]
        word=word[0:2]
        counts[word] = counts.get(word,0)+1


lst=list()
for value,count in counts.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print(value,count)
