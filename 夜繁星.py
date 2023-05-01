import turtle as t
import random  as r
t.speed(0)
t.colormode(255)


t.pensize(250)



for i in range(10):
    t.goto(-300,250-i*100)
    t.color(i*20,i*20,i*20)
    t.fd(1000)

##t.
# black sky
##t.colormode(255)
##t.bgcolor("black")
##t.pensize(100)
##
##
##t.goto(-300,200)
##t.forward(600)
##
##
##
##t.color(50,50,50)
##
##t.penup()
##t.goto(-400,100)
##t.pendown()
##t.forward(800)
##
##
##t.color(75,75,75)
##t.penup()
##t.goto(-400,0)
##t.pendown()
##t.forward(800)
##
##t.color(100,100,100)
##t.penup()
##t.goto(-400,-100)
##t.pendown()
##t.forward(800)
##
##t.color(125,125,125)
##t.penup()
##t.goto(-400,-200)
##t.pendown()
##t.forward(800)
##
##
##
##t.color(150,150,150)
##t.penup()
##t.goto(-400,-300)
##t.pendown()
##t.forward(800)

#star star
t.pensize(8)


for i in range(10):
    red=r.randint(180,255)
    green=r.randint(180,255)
    blue=0
    t.color(red,green,blue)   
    x=r.randint(-300,300)
    y=r.randint(0,250)
    
    
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.left(30)
        t.forward(15)
        t.right(120)
    t.end_fill()

