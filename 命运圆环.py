import turtle as t
import math
def yuan(r,n):
    t.circle(r,n)
r1=20
r2=48.3



r2=r1/(math.sqrt(2)-1)

for i in range(0,4):
    yuan(r1,90)
    t.rt(180)
t.rt(90)


# inner circle
yuan(r1,360)

yuan(r1,45)
yuan(-r2,45)

# big circle
t.lt(90)
yuan(r2,360)

#four yuanhu
t.lt(90)
for i in range(0,4):
    yuan(r2,90)
    t.rt(180)
