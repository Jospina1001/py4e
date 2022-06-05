
fh = open("mbox-short.txt")
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    number=float(line[19:30])
    count=number+count
    total=total+1

promedio=count/total
print("Average spam confidence:",promedio)
