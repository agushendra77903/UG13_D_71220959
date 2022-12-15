import turtle

t=turtle.Turtle()

def drawPersegi(xPos,yPos,lebar):
    t.up()
    t.goto(xPos,yPos)
    t.down()

t.screen.bgcolor('blue')

drawPersegi(0,0,200)
drawPersegi(-150,0,200)

t.pensize(15)
t.color('white')
t.circle(40)
t.circle(40,90)
t.right(5)
t.backward(100)
t.circle(40,-150)

drawPersegi(0,20,200)
drawPersegi(0,0,200)

t.goto(0,0)
t.pensize(15)
t.color('white')
t.right(45)
t.forward(100)

drawPersegi(0,0,200)
drawPersegi(150,0,200)

t.pensize(15)
t.color('white')
t.right(250)
t.circle(40)
t.circle(40,90)
t.right(5)
t.backward(100)
t.circle(40,-150)





drawPersegi(0,0,200)
drawPersegi(-50,85,200)

sc=turtle.Screen().exitonclick()
