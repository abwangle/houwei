import turtle as t
t.speed(0)
t.up()
t.goto(0,-50)
t.down()

t.begin_fill()
t.fillcolor('black')
t.circle (150,180)
t.circle(75,180)
t.circle(-75,180)
t.end_fill()

t.circle(-150,180)


t.up()
t.goto(0,160)
t.down()

t.begin_fill()
t.fillcolor('white')
t.circle (30,360)
t.end_fill()

t.up()
t.goto(0,0)
t.down()


t.begin_fill()
t.fillcolor('black')
t.circle (30,360)
t.end_fill()
##t.done()
##t.hideturtle ()


t.pensize(15)


##t.up()

t.goto(0,0)

##t.seth(-45)
t.up()
t.fd(180)
t.down()
t.right(90)
t.down()


t.fd(15)
t.fd(35)

t.up()
t.rt(180)
t.fd(50)
t.down()

t.fd(15)
t.fd(35)

t.up()
t.rt(90)
t.down()

t.fd(15)
t.fd(35)
t.fd(15)
t.fd(35)

t.up()
t.left(90)
t.fd(36)
t.lt(90)
t.down()


t.fd(35)
t.fd(15)
t.fd(15)
t.fd(35)

t.penup()
t.lt(180)
t.fd(50)
t.lt(90)
t.fd(50)
t.write('乾',font=(30))
