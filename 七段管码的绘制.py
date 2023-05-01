##import  turtle as t 
##def drawline(draw):
##    t.speed(1)
##    t.pendown() if draw else t .penup()
##    t.fd(40)
##    t.right(90)
##def drawdigit(digit):
##    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
##    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
##    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
##    drawline(True) if digit in [0,2,6,8] else drawline(False)
##    t.left(90)
##    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
##    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
##    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
##    t.left(180)
##    t.penup()
##    t.fd(20)
##def drawdate(date):
##    for i in date:
##        drawdigit(eval(i))
##def main():
##    t.setup(800,350,200,200)
##    t.penup()
##    t.fd(-300)
##    t.pensize(5)
##    drawdate('20181010')
##    t.hideturtle()
##    t.speed(0)
##    t.done()
##main()



import  turtle as t
import  time
def drawline(draw):
    t.speed(0)
    t.pendown() if draw else t .penup()
    t.fd(40)
    t.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawdate(date):
    t.pencolor('gold')
    for i in date:
        if i=='-':
            t.write('年',font=('Arial',18,'normal'))
            t.pencolor('green')
            t.fd(40)
        elif i=='=':
            t.write('月',font=('Arial',18,'normal'))
            t.pencolor('blue')
            t.fd(40)
        elif i=='+':
            t.write('日',font=('Arial',18,'normal'))
            t.pencolor('purple')
        else:
            drawdigit(eval(i))
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
##    drawdate('20181010')
    drawdate(time.strftime('%Y-%m=%d+',time.gmtime()))
    t.hideturtle()
    t.speed(0)
    t.done()
main()

    
    
