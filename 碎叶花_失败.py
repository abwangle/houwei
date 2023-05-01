from turtle import *

import random as r

def drawtree(length):
    if length>1:
        if length <30 and length>14:
            pensize(4)
    elif length<15   and  length>5:
        color('04B486')
        pensize(3)
    elif length<5   and   length>1:
        color('#FE2E9A')
        pensize(2)
    else:
        color('#5E5E5E')
        pensize(5)

    randangle=2*r.random()
    randlen=2*r.random()



    fd(length)
    right(20*randangle)
    drawtree(length-10*randlen)



    left(40*randangle)
    drawtree(length-10*randlen)


    right(20*randangle)
    
    up()
    backward(length)
    down()

def    fallingflowers(m):
    x,y=-1000,-750
    for i in range(30):
        up()
        goto(x,y)
        x+=100
        down()
        yval=50
        for i in range(m):
            a=100*r.random()
            b=2*r.random()
            print(a)
            if  a>59:
                color('#FE2E9A')
            else:
                color('#04B486')
            circle(5)
            
            up()
            goto(x,y+(yval*b))
            fd(a)
            yval+=50
            down()
        
setworldcoordinates(-1000,-750,1000,750)
tracer(False)


fallingflowers(10)
bgcolor('#F5F6CE')
color('#5E5E5E')
pensize(5)

up()
goto(0,-700)
down()

left(80)
fd(140)
drawtree(120)

input()
    
    
