import turtle as t

di=400
hou=30
num=11
size=10
d2=di-hou
r2=d2/2

t.dot(di,'#ff6600')
t.pensize(size)
t.pencolor('white')
t.fillcolor('#ff9900')

for i in range(num):
    t.speed(10)
    t.begin_fill()
    t.backward(r2)
    t.right(90)
    t.circle(r2,360/num)
    t.left(90)
    t.fd(r2)
    t.end_fill()
t.hideturtle()
input('锯子已画完，写任意字母退出：')

#test

##di=400
##t.dot(di,'#ff6600')
