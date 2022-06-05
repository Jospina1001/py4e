import turtle

sc=turtle.Screen()
sc.setup(600,600)
spiral=turtle.Turtle()
sc.bgcolor("black")
col=("yellow","blue","white","green")
c=0

for i in range(100):
    spiral.forward(i*10)
    spiral.right(120)
    spiral.color(col[c])
    if c==3:
        c=0
    else:
        c+=1
