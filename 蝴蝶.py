import turtle as t

def hu(r,n):
##     for i in range(0,n):   '循环制作
##         t.fd(0.0174*r)
##         t.rt(1)
     t.begin_fill()
     t.color('yellow')
     t.circle(-r,n)  #'圆形制作
     t.end_fill()
def die(r,n):
##        for i in range(0,n):
##            t.fd(0.0174*r)
##            t.lt(1)
     t.begin_fill()
     t.color('green')
     t.circle(r,n)
     t.end_fill ()
t.lt(90)

die(10,360)
die(20,360)
hu(10,360)
hu(20,360)

t.fd(80)
die(20,360)
die(40,360)
hu(20,360)
hu(40,360)

t.fd(50)
die(20,90)
die(10,360)

t.lt(180)
hu(20,90)

t.lt(180)
hu(20,90)
hu(10,360)
