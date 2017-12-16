import turtle

myTurtle = turtle.Turtle()
count = 0

while count in range(0, 3):
    myTurtle.forward(50)
    myTurtle.left(120)
    count = count + 1

turtle.done()
