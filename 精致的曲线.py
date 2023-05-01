###方案1
##import turtle as t
##def banyuan(r):
##    
##    for i in range(0,180):
##        for i in range(0,180):
##            t.fd(0.0174*r)
##            t.rt(1)
##    return
####图案1
##n=5
####图案2
####n=4
######图案3
####n=5
##
##t.speed(0)
##t.lt(90)
##for i in range(0,n):
##    banyuan(50)
##    t.rt((n-2)*180/n)
    
#方案2
import turtle as t
def banyuan1(r):
    t.circle(-r,180)
    return

####图案1
##n=3
####图案2
##n=4
##图案3
n=5
t.speed(1)
t.lt(10)
for i in range(0,n):
    banyuan1(50)
    t.rt((n-2)*180/n)
