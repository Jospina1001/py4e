hrs = input("Ingrese Horas:")
h = float(hrs)

tar = input("Ingrese tarifa:")
t = float(tar)

def computepay(a,b):
        if(a<=40):
            paga=a*b
            return paga
        elif(a>40):
           paga=((a-5)*b)+((a-40)*b*1.5)
           return paga

p =computepay(h,t)
print(p)
