#one
##import turtle as t
##def kono(size,n):
##    if n ==0:
##        t.fd(size)
##    else:
##        for angle in [0,60,-120,60]:
##            t.left(angle)
##            kono(size/3,n-1)
##def main():
##    t.setup(800,400)
##    t.penup()
##    t.goto(-300,-50)
##    t.pendown()
##    t.pensize(2)
##    kono(600,3)
##    t.hideturtle()
##main()
#two
import turtle as t
def kono(size,n):
    if n ==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            kono(size/3,n-1)
def main():
    t.speed(0)
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    leval=4
    kono(400,leval)
    t.right(120)
    kono(400,leval)
    t.right(120)
    kono(400,leval)
   
    
    t.hideturtle()
main()
