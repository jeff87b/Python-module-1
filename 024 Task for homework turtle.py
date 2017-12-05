import turtle

myTurtle = turtle.Turtle()
count = 0

starSize = int(input("Enter the size of the star: "))

while count in range(0, 5):
    myTurtle.forward(starSize)
    myTurtle.right(144)
    count = count + 1

turtle.done()
