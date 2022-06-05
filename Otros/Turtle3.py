import turtle

col= ("red","yellow","green","red","yellow","green")

t=turtle.Turtle()

screen=turtle.Screen()
screen.bgcolor("black")
t.speed(30)

for i in range(500):
    t.color(col[i%6])
    t.forward(i*1.5)
    t.left(118)
    t.width(3)
