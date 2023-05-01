# one
from turtle import *
from random import *
from math import *
def tree(n,m):
    # 阴影效果
    pd()    #下笔
    t=cos(radians(heading()+45))/8+0.25  #
    pencolor(t,t,t)
    pensize(n/3)
    forward(m)    #画树枝
    
if n>0:
    b=random()*15+10   #右分支偏转角度
    c=random()*15+10   #左分支偏转角度
    d=L*(random()*0.25+0.7)  #下一个分支的长度
    #右转一定角度，画右分支
    right(b)
    tree(n-1,d)
    #左转一定角度，画左分支
    left(b+c)
    tree(n-1,d)
    # 转回来
    right(c)
else:
    # 画叶子
    right(90)
    n=cos(radians(heading()-45))/4+0.5
    pencolor(n,n*0.8,n*0.8)
    circle(3)
    left(90)

# 添加0.3倍的飘落的叶子    
if (random()>0.7):
    # 飘落
    pu()
    t=heading()
    an=-40+random()*40
    setheading(an)
    dis=int(800*random()*0.5+400*random()*0.3+200*random()*0.2)
    forward(dis)
    setheading(t)
    # 画叶子
    pd()
    right(90)
    n=cos(radians(heading()-45))/4+0.5
    pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
    circle(2)
    left(90)
    
    pu()
    # 返回
    t=heading()
    setheading(an)
    backward(dis)
    setheading(t)
    
    pu()
    backward(L)  #返回
    
    bgcolour(0.5,0.5,0.5) #背景色
    ht()
    speed(0)
    tracer(0,0)
    
    pu()  #抬笔
    backward(100)
    left(90)
    pu()
    backward(300) #后退300
    tree(12,100)  #递归7层
    done()



###two
##from turtle import *
##from random import *
##from math   import *
##def tree(n,m):
##    pd()
##    t=cos(radians(heading()+25))/8+0.25
##    pencolor(n/4)
##    forward(m)
####    if n>0:
####        b=random()*15+10
####        c=random()*15+10
####        forward(m)
##    if n>0:
##        b=random()*15+10
##        c=random()*15+10
##        d=m*(random()*0.35+0.6)
##        tree(n-1,d)
##        left(b+c)
##        tree(n-1,d)
##        right(c)
##    else:
##        right(90)
##        n=cos(radians(heading()-45))/4
##        pencolor(n,n,n)
##        circle(2)
##        left(90)
##    pu()
##    backward(m)
##    bgcolor(0.5,0.5,0.5)
##    ht()
##    speed(0)
##    tracer(0,0)
##    left(90)
##    pu()
##    backward(300)
##    tree(13,100)
##    done()

    
    
    
