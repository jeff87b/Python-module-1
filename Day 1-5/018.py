import turtle

myTurtle = turtle.Turtle()
count = 0

while count in range(0, 4):
    myTurtle.forward(50)
    myTurtle.left(90)
    count = count + 1

turtle.done()
