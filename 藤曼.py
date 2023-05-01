import turtle as t
##
def yuanhu(r,n):
##    for i in range(0,n):
##        t.fd(0.0174*r)
##        t.rt(70)
##        t.lt(70)
      t.color('pink')
      t.circle(-r,n)
def yuanhu1(r,n):

      t.color('darkgreen')
      t.circle(-r,n)
      return


def yezi(r,n):
    for i in range(0,2):
        t.begin_fill ()
        t.color('lightgreen')
        yuanhu1(r,n)
        t.rt(180-n)
        t.end_fill ()
    return



def letus(r,n):
    for i in range(0,2):
##        t.begin_fill ()
##        t.color('pink')
        yuanhu(r,n)
        t.rt(180-n)
##        t.end_fill ()
    return

t.speed(0)
t.up()
t.goto(-500,-300)
t.down()

n=8
t.lt(90)
t.bgcolor ('lightyellow')
for i in range(0,n):
    t.pensize(4)
    yuanhu(300,150/n)
    t.lt(90)
    yezi(25,90)
    t.rt(90)
    yezi(25,90)
        
for i in range(0,n):
    yuanhu1(-300,150/n)
    t.lt(90)
    yezi(25,90)
    t.rt(90)
    yezi(25,90)

    
t.up()
t.goto(100,-20)
t.down()

    
t.rt(180)
t.pensize(10)
t.pencolor ('darkgreen')
t.bk(200)
t.rt(90)


for i in range(0,4):
    
    letus(150,90)
    t.rt(30)


