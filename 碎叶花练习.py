import turtle  as t
import random  as r

##t.color('#5E5E5E')
##t.pensize(6)

# set color and pensize

##t.left(80)
##t.fd(100)
##t.rt(30)
##t.fd(30)
##t.rt(30)
##t.fd(30)



# trail1
##def drawtree(length):
##        t.right(20)
##        t.fd(length)
##        
##        
##t.color('#5E5E5E')
##t.pensize(5)
##
##
##t.up()
##t.goto(0,-300)
##t.down()
##
##
####t.up()
####t.goto(0,0)
####t.down()
##
##t.left(80)
##t.fd(140)
##drawtree(210)
##input





#set treetruck funcition   recursion
##def drawtree(length):
##    if length>1:
##        randangle=r.random()  #随机角度的设置
##        randlen=r.random()   #随机修正纸条的长度
##
##        
##        t.right(20*randangle) #随机变换角
##        t.fd(length-10*randlen)
##       
##        
##        t.up()
##        t.bk(length) #返回原树枝点
##        t.down()
##
##         
##        t.left(40*randangle)    #新加
##        t.fd(length)
##        drawtree(length-10*randlen) #随机枝条
##


# 改良版2

def drawtree(length):
    if length>1:
        if length<30 and length>14:
            t.pensize(4)
        elif length<15 and length>5:
            t.color('#04B486')
            t.pensize(3)
        elif length<5  and length>1:
            t.color('#FE2E9A')
            t.pensize(2)
        else:
            t.color('#5E5E5E')
            t.pensize(5)
        
        t.speed(0)
        randangle=r.random()  #随机角度的设置
        randlen=r.random()   #随机修正纸条的长度

        t.fd(length)
        t.right(30*randangle) #随机变换角
##        t.fd(length-10*randlen)
        drawtree(length-10*randlen)

         
        t.left(60*randangle)    #新加
        drawtree(length-10*randlen) #随机枝条
        t.right(30*randangle)


        
        t.up()
        t.bk(length) #返回原树枝点
        t.down()
        

t.tracer(False)        
t.color('#5E5E5E')
t.pensize(5)


t.up()
t.goto(0,-520)
t.down()


##t.up()
##t.goto(0,0)
##t.down()

t.left(80)
t.fd(140)
drawtree(65)
input
    
