import turtle

myTurtle = turtle.Turtle()
count = 0
count2 = 0
count3 = 0

while count in range(0, 4):
    myTurtle.forward(50)
    myTurtle.left(90)
    count = count + 1

myTurtle.left(225)
myTurtle.penup()
myTurtle.forward(50)
myTurtle.pendown()
myTurtle.left(135)

while count2 in range(0, 4):
    myTurtle.forward(118)
    myTurtle.left(90)
    count2 = count2 + 1

myTurtle.left(225)
myTurtle.penup()
myTurtle.forward(50)
myTurtle.pendown()
myTurtle.left(135)

while count3 in range(0, 4):
    myTurtle.forward(190)
    myTurtle.left(90)
    count3 = count3 + 1

turtle.done()
