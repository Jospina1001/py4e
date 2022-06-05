hrs = input("Ingrese Horas:")
h = float(hrs)

tar = input("Ingrese tarifa:")
t = float(tar)

if(h<=40):
	paga=h*t
elif(h>40):
    paga=((h-5)*t)+((h-40)*t*1.5)

print("Paga:",paga)
