import turtle as t
import math
def yuanhu(r,n):
    t.pencolor('teal')
    t.circle(-r,n)
    return

def youquxian(r,n):
    for i in range(2):
        t.begin_fill()
        t.color('deeppink')
        yuanhu(r,n)
        yuanhu(-r,n)
        t.end_fill()
    return

def zuoquxian(r,n):
    for m in range(2):
        yuanhu(-r,n)
        yuanhu(r,n)
    return

t.bgcolor('lavender')
t.speed(0)
t.up()
##t.goto(0,300)
t.goto(-200,100)
t.down()


t.rt(30)


for i in range(0,9):
    zuoquxian(100,100)
    t.rt(180-20)
